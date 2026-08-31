# Kunlun Li — Personal Research Website

Source code for [kunlunli-firefly.github.io](https://kunlunli-firefly.github.io), an English-first personal research portfolio covering medical imaging, machine learning, computer vision, and signal processing.

The site keeps Firefly's visual identity while organizing Kunlun Li's work as structured, extensible content. It includes Research, Projects, Publications, Blog, About, and a sanitized public CV.

## Content structure

- `src/content/projects/` — structured project records and detail pages
- `src/content/publications/` — publications, preprints, and manuscripts
- `src/content/posts/` — technical notes and project reflections
- `src/config/` — site identity, navigation, profile, wallpaper, and theme settings
- `public/cv/` — sanitized public CV only

Projects and publications use typed Astro content collections, so future entries can be added as Markdown without rebuilding page layouts.

## Local development

Requirements:

- Node.js 22.23 or newer
- pnpm 11.22.0

```bash
pnpm install
pnpm dev
```

Before publishing:

```bash
pnpm check
pnpm type-check
pnpm build
```

The GitHub Pages workflow publishes the production output from the `main` branch.

## Privacy boundary

The repository intentionally excludes transcripts, test reports, Personal Statements, private addresses, phone numbers, and other application records. Only the sanitized public CV is included.

## Theme and visual attribution

This site is adapted from the open-source [Firefly](https://github.com/CuteLeaf/Firefly) Astro theme, which is based on [Fuwari](https://github.com/saicaca/fuwari). The upstream license and code attribution are retained.

Firefly character images and related game assets remain the property of miHoYo, the developer of *Honkai: Star Rail*. They are used here as retained theme visuals; no ownership of those assets is claimed.
