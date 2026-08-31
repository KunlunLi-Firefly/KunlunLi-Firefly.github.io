# Firefly Personal Website Migration Report

Date: 2026-08-31
Status: Local website and sanitized public CV complete; GitHub deployment in progress.

## 1. Outcome

A new Astro/Firefly personal research website has been prepared locally. It is structured for future growth rather than as a one-time copy of the previous repository.

The current site contains:

- A professional English-first landing page
- Research, Projects, Publications, Blog, and About sections
- Five structured project entries
- Three structured publication entries
- One site-note blog post
- A reusable content schema for future projects and publications
- Selected project figures and an owner-provided public profile photograph
- Firefly character wallpapers, light/dark logo assets, and a desktop Spine companion
- Confirmed public email: `lkl2654462334@outlook.com`
- A one-page sanitized public CV with the owner-provided portrait
- No transcript, test report, application essay, or other private document

No online GitHub repository was modified during this work.

## 2. Source setup

The new site was created from Firefly v6.16.5. The template remote was renamed to `upstream`, leaving `origin` available for the future personal repository.

Commands used:

```bash
git clone --depth 1 --branch v6.16.5 https://github.com/CuteLeaf/Firefly.git firefly-personal-website
cd firefly-personal-website
git remote rename origin upstream
pnpm install
```

Why this matters:

- `--depth 1` downloads only the selected template snapshot and keeps the new project small.
- `--branch v6.16.5` pins the exact template version used for this migration.
- Renaming the remote preserves a clean distinction between the template source (`upstream`) and the future personal repository (`origin`).

## 3. Content architecture

Two typed Astro content collections were added in `src/content.config.ts`:

- `projects`: title, summary, year, status, research area, methods, datasets, evidence, role, collaborators, cover, order, and links
- `publications`: title, authors, year, venue, publication type, status, summary, DOI, URL, and order

This design allows future filtering, sorting, and dedicated detail pages without rewriting each page layout.

New reusable UI files:

- `src/components/portfolio/ProjectCard.astro`
- `src/components/portfolio/PublicationCard.astro`

New routes:

- `src/pages/index.astro`
- `src/pages/research.astro`
- `src/pages/projects/index.astro`
- `src/pages/projects/[slug].astro`
- `src/pages/publications/index.astro`
- `src/pages/blog/index.astro`

## 4. Migrated material

| Area | Migrated as | Public evidence boundary |
| --- | --- | --- |
| Liver and tumor segmentation | Project page and selected figure | Dataset-specific project results; no clinical claim |
| MRI subarachnoid-space analysis | Coursework project page and figure | Methods and learning outcomes; no unverified clinical conclusion |
| Epoch extraction | Project and publication entries | arXiv metadata and reported experiment context |
| Skin-lesion analysis | Project page and figure | Explicitly labeled preliminary/exploratory |
| SSLAL sign-language recognition | Project and manuscript entries | Explicitly labeled as an unpublished manuscript that is not yet a preprint; PDF link removed |
| Absolute-value detector | Publication entry | DOI metadata verified against the publisher record |

Project reports were not copied into the new public site. Collaborative manuscripts and reports remain withheld unless sharing rights and current publication status are confirmed.

## 5. Professionalization changes

The theme was adjusted to keep Firefly's visual identity while removing unrelated demo functions.

- Random Firefly desktop and mobile wallpapers were restored in banner mode.
- Firefly light/dark logo assets were restored while keeping the site title as Kunlun Li.
- The Firefly Spine companion was restored on desktop and remains hidden on mobile to avoid covering content.
- The owner-provided profile photograph remains the personal identity image.
- The background video remains disabled.
- Music player remains disabled in the navigation and sidebar.
- Sponsor, friends, guestbook, gallery, dynamics, and bookmark pages remain disabled.
- Demo blog posts and template tutorial content were removed.
- Multi-widget sidebars were replaced with a focused profile sidebar.
- Template title, profile text, keywords, and default navigation were replaced.

Firefly character images are credited to miHoYo, following the upstream theme's copyright notice. Firefly/Fuwari code attribution and licensing are retained.

The navigation is now:

`Research → Projects → Publications → Blog → About → GitHub`

The site title itself links to the home page, so a separate Home item is unnecessary.

## 6. Privacy boundary

The public-site policy applied in this migration is:

- Publish only the sanitized public CV; keep transcripts, test reports, and application essays private.
- Do not publish transcripts, test reports, Personal Statement/application essays, or private records.
- Use only the owner-confirmed degree, affiliation, contact, and location. Do not infer an unconfirmed job title.
- Do not link collaborative manuscripts or reports until status and sharing rights are confirmed.

Final scans of the source content, public assets, and built website found none of the following:

- PDF, Word, or Excel documents
- Transcript or test-score material
- Personal Statement or Statement of Purpose content
- GRE, GPA, TOEFL, or IELTS information

The confirmed public email is intentionally included and is encoded in rendered Markdown links to reduce basic address scraping.

Important: this result applies to the new local website. The old online repository and its Git history have not been cleaned.

## 7. Validation performed

Commands used:

```bash
pnpm exec biome format --write <changed files>
pnpm check
pnpm type-check
pnpm build
pnpm preview --host 127.0.0.1 --port 4321
```

Final results:

- Astro check: 255 files, 0 errors, 0 warnings, 0 hints
- TypeScript check: passed
- Production build: passed
- Static output: 32 pages
- Search index: 7 content pages
- Browser console: no errors or warnings on tested pages
- Desktop viewport: no horizontal overflow or broken images
- Mobile viewport (390 × 844): no horizontal overflow or broken images

The build prints two non-blocking template notices: there is no custom `src/icons` directory, and some shared template JavaScript chunks exceed 500 kB. They do not prevent deployment.

## 8. Local development commands

Run the site locally:

```bash
pnpm install
pnpm dev
```

Before publishing a change:

```bash
pnpm check
pnpm type-check
pnpm build
```

Preview the exact production output:

```bash
pnpm preview
```

Content is added by creating Markdown files in:

- `src/content/projects/`
- `src/content/publications/`
- `src/content/posts/`

## 9. Owner confirmation required before the next stage

The following decisions cannot be safely inferred and must still be provided by Kunlun Li:

1. SSLAL sharing rights after the planned arXiv upload, including whether collaborators approve linking the preprint and related project materials.
2. Authorization for old-repository cleanup: history rewriting is destructive for existing clones and must be explicitly approved before removing sensitive files from Git history.

## 10. Recommended next sequence

Current sequence:

1. Generate and visually verify the sanitized public CV. (Complete)
2. Add CV download links to the profile, landing page, and About page. (Complete)
3. Perform one more privacy, build, and link scan.
4. Create the confirmed public repository `KunlunLi-Firefly.github.io` and deploy to `https://kunlunli-firefly.github.io`.
5. Verify the live domain, links, search, CV download, and mobile layout.
6. After the planned arXiv upload, update SSLAL status and links with collaborator approval.
7. If separately authorized, remove sensitive files from the old repository history.
