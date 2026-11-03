# Contributing to DCA

Thanks for helping keep this guide useful! Most contributions are small: fixing a broken link, swapping in a better resource, or correcting a typo. All of them are welcome.

## How the guide is organised

- [`README.md`](README.md) is the index: exam details, useful links and the table of domains.
- Each exam domain has its own file, and every bullet is an objective from the [official study guide](https://a.storyblok.com/f/146871/x/2001ce939c/docker-study-guide_v1-5-jan-2025.pdf) linked to a resource that covers it:
  - [`domain1-orchestration.md`](domain1-orchestration.md)
  - [`domain2-image-management.md`](domain2-image-management.md)
  - [`domain3-installation.md`](domain3-installation.md)
  - [`domain4-networking.md`](domain4-networking.md)
  - [`domain5-security.md`](domain5-security.md)
  - [`domain6-storage.md`](domain6-storage.md)

The site at [evalle.github.io/DCA](https://evalle.github.io/DCA/) is built from these files by GitHub Pages, so a merged change goes live automatically.

## Adding or changing a link

1. Find the objective in the right domain file. Keep the objective text as it appears in the official study guide.
2. Prefer official documentation: [Docker docs](https://docs.docker.com/), [Mirantis docs](https://docs.mirantis.com/) for UCP/MKE and DTR/MSR, and [Kubernetes docs](https://kubernetes.io/docs/) for the Kubernetes objectives. Use a blog post or tutorial only when the official docs don't cover the topic well.
3. Use the page's current URL, not one that redirects. If you link to a section, check that the `#anchor` exists on the page.
4. If the original article is gone, link to a [Wayback Machine](https://web.archive.org/) snapshot rather than removing the objective.
5. An objective can have more than one link when it covers several things, for example:

   ```markdown
   - Compare and contrast "host" and "ingress" publishing modes ([Host](https://...), [Ingress](https://...))
   ```

## Link checking

Every pull request and push to `master` runs the [Check Markdown links](.github/workflows/action.yml) workflow, which also runs weekly. It fails if any link in a `.md` file is dead or points to a missing anchor. Settings, such as ignored URLs, live in [`.mlc.config.json`](.mlc.config.json).

To run the same check locally:

```sh
npx markdown-link-check@3.14.2 -c .mlc.config.json domain1-orchestration.md
```

## Submitting a change

1. Fork the repository and create a branch.
2. Make your change and run the link check on the files you touched.
3. Open a pull request against `master` that says what changed and why, for example "Docker moved this page" or "this article covers the objective better".

## Reporting a problem

Found a broken link, an outdated resource or a missing objective, but don't have time to fix it? [Open an issue](https://github.com/Evalle/DCA/issues/new/choose) and pick **Broken or outdated link** or **Suggest a resource**. The form asks for the details we need.

## Legal notice

By contributing, you confirm that you authored the content, that you have the right to contribute it, and that it may be provided under the project's [license](LICENSE).
