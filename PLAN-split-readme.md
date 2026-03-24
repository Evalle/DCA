# Plan: Split README.md into Per-Domain Files

## Goal

Replace the monolithic `README.md` with a lean index that links to six per-domain markdown files — one per exam domain. Improves readability, makes contributions easier, and gives each domain a dedicated URL on the GitHub Pages site.

---

## New File Structure

```
README.md                    ← rewritten as lean index
domain1-orchestration.md     ← Domain 1: Orchestration (25%)
domain2-image-management.md  ← Domain 2: Image Creation, Management, and Registry (20%)
domain3-installation.md      ← Domain 3: Installation and Configuration (15%)
domain4-networking.md        ← Domain 4: Networking (15%)
domain5-security.md          ← Domain 5: Security (15%)
domain6-storage.md           ← Domain 6: Storage and Volumes (10%)
```

No `docs/` subdirectory needed. Jekyll/Slate serves all root-level `.md` files automatically. Each domain file will be available at `https://evalle.github.io/DCA/domain1-orchestration/` etc.

---

## New README.md (Index)

Keeps:
- CI badge + stars sparkline
- Introduction paragraph + web version link
- "Important Info" block (product renames affect multiple domains, so it stays global)
- Exam Details section
- Useful Links section
- Preparation + Contributors sections

Replaces the current wall-of-links with a summary navigation table:

```markdown
## Exam Domains

| Domain | Weight | Study Guide |
|--------|--------|-------------|
| Domain 1: Orchestration | 25% | [Study →](domain1-orchestration.md) |
| Domain 2: Image Creation, Management, and Registry | 20% | [Study →](domain2-image-management.md) |
| Domain 3: Installation and Configuration | 15% | [Study →](domain3-installation.md) |
| Domain 4: Networking | 15% | [Study →](domain4-networking.md) |
| Domain 5: Security | 15% | [Study →](domain5-security.md) |
| Domain 6: Storage and Volumes | 10% | [Study →](domain6-storage.md) |
```

---

## Each Domain File

Content extracted **verbatim** from the current README. Navigation footers added top and bottom.

### Template

```markdown
# Domain N: <Name> (<weight>% of exam)

[← Back to Study Guide Index](README.md)

- [link 1]
- [link 2]
- ...

---

[← Domain N-1](domain(n-1)-name.md) | [Back to Index](README.md) | [Next: Domain N+1 →](domain(n+1)-name.md)
```

### Per-file navigation footers

| File | Footer |
|------|--------|
| `domain1-orchestration.md` | `[← Back to Index](README.md)` \| `[Next: Domain 2 →](domain2-image-management.md)` |
| `domain2-image-management.md` | `[← Domain 1](domain1-orchestration.md)` \| `[Back to Index](README.md)` \| `[Next: Domain 3 →](domain3-installation.md)` |
| `domain3-installation.md` | `[← Domain 2](domain2-image-management.md)` \| `[Back to Index](README.md)` \| `[Next: Domain 4 →](domain4-networking.md)` |
| `domain4-networking.md` | `[← Domain 3](domain3-installation.md)` \| `[Back to Index](README.md)` \| `[Next: Domain 5 →](domain5-security.md)` |
| `domain5-security.md` | `[← Domain 4](domain4-networking.md)` \| `[Back to Index](README.md)` \| `[Next: Domain 6 →](domain6-storage.md)` |
| `domain6-storage.md` | `[← Domain 5](domain5-security.md)` \| `[Back to Index](README.md)` |

---

## Files That Do NOT Change

| File | Reason |
|------|--------|
| `.github/workflows/action.yml` | Link checker already scans all `*.md` files — new domain files are automatically covered |
| `.mlc.config.json` | The one ignored StackOverflow URL lives in Domain 2 content; stays unchanged |
| `_config.yml` | Slate theme serves root-level `.md` files natively; no config changes needed |
| `CONTRIBUTING.md` | Stays as-is (optional follow-up: add a note about per-domain file structure for contributors) |
| `LICENSE` | Unchanged |

---

## Order of Implementation

1. Create `domain1-orchestration.md` (adds content, breaks nothing)
2. Create `domain2-image-management.md`
3. Create `domain3-installation.md`
4. Create `domain4-networking.md`
5. Create `domain5-security.md`
6. Create `domain6-storage.md`
7. Rewrite `README.md` as the lean index (done last — removes domain content, adds nav table)

**Why this order:** steps 1–6 only add files. Step 7 is the only destructive change. If the PR is reviewed mid-apply, readers are never left with broken links.

---

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Content accidentally dropped during split | Low | Content is verbatim extraction; git diff of old README vs. new README + domain files must show zero net content deletions |
| GitHub Pages relative links breaking | Low | Jekyll resolves `.md` relative links correctly with Slate theme |
| CI link checker failing on inter-file nav links | Low | Local file links (e.g. `domain1-orchestration.md`) are resolved as file existence checks — will pass once files exist |
| External sites linking to README anchors (e.g. `#domain-1-orchestration-25-of-exam`) | Very Low | Unlikely; acceptable break — the heading still exists in the domain file with the same anchor |
