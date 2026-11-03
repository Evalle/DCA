#!/usr/bin/env python3
"""Find links that still return 200 but no longer point at the right content.

markdown-link-check only looks at the final HTTP status, so it misses:
  * links that redirect to a site's home or landing page (the page was removed),
  * links that redirect to a different page (the page moved),
  * #anchors that no longer exist on the target page.

Usage: check_link_targets.py [FILE.md ...]   (defaults to every *.md in the repo root)
Writes a Markdown report to stdout and exits 1 if anything needs fixing.
"""

import concurrent.futures
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)
# Hosts that rate-limit or block automated requests; markdown-link-check covers them.
SKIP_HOSTS = {"web.archive.org", "stackoverflow.com"}
# Redirect targets that mean "this page is gone" even though they are deep paths.
LANDING_PATHS = {"/welcome", "/retired", "/search"}
LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)")
CODE_BLOCK_RE = re.compile(r"^[ \t]*```.*?^[ \t]*```", re.S | re.M)
# Some sites (docs.mirantis.com) answer bots with a 200 challenge page instead
# of the real content, so anchors and redirects can't be judged.
CHALLENGE_MARKERS = ("_Incapsula_Resource", "challenge-platform", "<title>Just a moment...</title>")
LOGIN_PATH_RE = re.compile(r"/(login|signin|sign-in|session/new)\b")


def normalise(url):
    """Ignore differences that don't change the page: scheme, www., trailing slash, .html."""
    parts = urllib.parse.urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/").removesuffix(".html").rstrip("/")
    return host, path


def is_landing_page(url):
    path = urllib.parse.urlsplit(url).path.rstrip("/")
    return path.count("/") <= 1 or path in LANDING_PATHS


def has_anchor(html, fragment):
    pattern = r"""(?:id|name)=["']?(?:user-content-)?%s["'\s>]""" % re.escape(fragment)
    return re.search(pattern, html) is not None


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", "replace")
                return response.status, response.geturl(), body
        except urllib.error.HTTPError as error:
            if error.code in (429, 503) and attempt < 2:
                time.sleep(10 * (attempt + 1))
                continue
            return error.code, url, ""
        except Exception as error:  # timeouts, DNS, TLS
            if attempt < 2:
                time.sleep(5)
                continue
            return f"error: {error.__class__.__name__}", url, ""


def check(url):
    base, _, fragment = url.partition("#")
    status, final, body = fetch(base)
    if status != 200:
        # Dead links are markdown-link-check's job; just note we couldn't verify.
        return "unchecked", f"HTTP {status}"
    if any(marker in body for marker in CHALLENGE_MARKERS):
        return "unchecked", "bot challenge page"
    if LOGIN_PATH_RE.search(urllib.parse.urlsplit(final).path) and not LOGIN_PATH_RE.search(base):
        return "unchecked", "requires sign-in"
    if normalise(final) != normalise(base):
        if is_landing_page(final):
            return "removed", final
        return "moved", final
    if fragment and not has_anchor(body, fragment):
        return "anchor", fragment
    return "ok", ""


def main(paths):
    files = [pathlib.Path(p) for p in paths] or sorted(pathlib.Path(".").glob("*.md"))
    links = {}  # url -> files it appears in
    for file in files:
        text = CODE_BLOCK_RE.sub("", file.read_text(encoding="utf-8"))
        for url in LINK_RE.findall(text):
            if urllib.parse.urlsplit(url).netloc.lower() not in SKIP_HOSTS:
                links.setdefault(url, set()).add(file.name)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = dict(zip(links, pool.map(check, links)))

    sections = {
        "removed": ("Redirects to a landing page (page probably removed)", "lands on"),
        "moved": ("Redirects to a different page (update to the new URL)", "now at"),
        "anchor": ("Section anchor missing on the target page", "missing"),
    }
    problems = 0
    print(f"Checked {len(links)} links in {len(files)} files.\n")
    for kind, (heading, label) in sections.items():
        rows = sorted((url, info) for url, (k, info) in results.items() if k == kind)
        if not rows:
            continue
        problems += len(rows)
        print(f"### {heading}\n")
        for url, info in rows:
            where = ", ".join(sorted(links[url]))
            detail = f"`#{info}`" if kind == "anchor" else f"<{info}>"
            print(f"- `{where}`: <{url}> ({label} {detail})")
        print()

    unchecked = sorted((url, info) for url, (k, info) in results.items() if k == "unchecked")
    if unchecked:
        print("<details><summary>Could not verify (blocked or down; not counted as failures)</summary>\n")
        for url, info in unchecked:
            print(f"- <{url}>: {info}")
        print("\n</details>")

    if not problems:
        print("No moved, removed or broken-anchor links found.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
