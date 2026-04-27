# Cowork → Claude Code handoff

Written by Claude in Cowork mode at the end of a long session, for whoever picks this up next (likely Claude Code running locally on Andrew's Mac, or Andrew working in the codebase directly).

## What this session accomplished

1. **Stage 2 imagery for Advaita Vedanta** — generated 17 Imagen 4 images, did a QA pass, regenerated 8 with text/watermark/wrong-subject artifacts. All clean now under `public/images/`.
2. **Christian Mysticism tradition built end to end** — 1 tradition page, 14 teacher pages (8 full, 6 biographical-only including the 4 Rhineland women + Bede Griffiths + Anthony de Mello), 10 text pages with frontmatter and sample passages. All in the same voice as the Advaita pages.
3. **Christian Mysticism imagery** — 25 Imagen 4 images (1 hero, 14 portraits, 10 text symbols), QA pass, 4 regenerations for misfires (Hildegard came back as a tiger first time, Hadewijch as a modern beach photo, Marguerite Porete as a cake — all fixed by removing the proper names from prompts and describing the appearance generically).
4. **Node.js installed on Andrew's Mac** via the official .pkg installer. Hit the well-known npm bug #4828 (missing `@rollup/rollup-darwin-arm64`); fixed by `npm install @rollup/rollup-darwin-arm64`. Dev server now runs.
5. **Brand refresh to mirror the existing soulspiritself.com** — extracted the orb logo from the live site (`public/images/soul-spirit-self-logo.png`), pulled the exact teal palette (#1a4a65 → #2a6a88 → #3278a0) and gold accent (#c9a96e), rebuilt the homepage to match the existing layout flow (logo → "SOUL SPIRIT SELF" wide-spaced title → "A Journey Within" tagline → Watch Now CTA → Featured videos → Traditions library → Daily Contemplation → Email signup).
6. **New routes** — `/watch/`, `/teachers/`, `/texts/`, `/about/` index pages, plus `Nav` and `Footer` updated with the orb logo.
7. **New components** — `VideoCard.astro`, `EmailSignup.astro`, `DailyContemplation.astro`.
8. **Video data file** — `src/data/videos.ts` lists the 9 YouTube videos pulled from the existing site. Edit this file to add/remove/reorder videos; both the homepage Featured grid and `/watch/` read from it.

## Known small bugs to fix next

1. **Page title doubled.** Pages other than the homepage are showing "Watch — Soul Spirit Self — Soul Spirit Self" in the tab title. Look at `src/layouts/BaseLayout.astro` line 14 — the page templates are passing `title="Watch — Soul Spirit Self"` which then gets the suffix appended. Fix: pages should pass just the page name, e.g. `title="Watch"`, and let BaseLayout add the site suffix. Affected files: `src/pages/watch.astro`, `src/pages/teachers/index.astro`, `src/pages/texts/index.astro`, `src/pages/about.astro` (`about.astro` is already correct, the others need their `title=` props simplified).
2. **Hero crowding at large widths.** The "Welcome to Soul Spirit Self…" blurb on the homepage runs slightly close to the "SOUL SPIRIT SELF" title above it on very wide viewports. Easy CSS fix in `src/pages/index.astro`.
3. **Imagen 4 hero badge still visible.** The tradition pages render an `IMAGEN 4 HERO` development tag in the corner of the hero. Search for `hero-imagen-tag` in `src/pages/traditions/[slug].astro` and remove or gate behind `import.meta.env.DEV`.

## Email signup is wired but not connected

`src/components/EmailSignup.astro` reads a `PUBLIC_KIT_FORM_ID` environment variable. If it isn't set, the form action is `#` (does nothing). To activate:

1. Get the form ID from your Kit (formerly ConvertKit) account.
2. Add a line to `.env`: `PUBLIC_KIT_FORM_ID=your_id_here`
3. Restart the dev server.

Alternatively swap to Mailchimp or Netlify Forms by editing the component's form action.

## Where the dev server lives

Run from `~/Documents/soul-spirit-self-handover-bundle/soul-spirit-self`:

```
npm run dev
```

Serves at http://localhost:4321. Auto-reloads on file changes. Stop with Ctrl+C.

## What I'd suggest doing next

In rough order of return-on-effort:

1. Fix the three small bugs above (15 minutes total).
2. Wire up the Kit form ID.
3. Decide whether teacher pages should have their own URLs (currently they render only as cards on the tradition page; there's an empty `src/pages/teachers/` directory ready for a `[slug].astro` route).
4. Set up GitHub + Netlify and push live. The `netlify.toml` is already correct.
5. Either populate the next tradition (Buddhist Nonduality is the natural next choice given PD coverage) or write the first 3 journal posts to seed a `/journal/` section.

## Things that were tricky in Cowork that won't be in Claude Code

- The Cowork bash sandbox is a separate Linux machine. `npm install` results don't carry over to the user's Mac, which is why we hit the rollup bug. Claude Code runs in your real shell, so this won't repeat.
- Chrome MCP screenshot timeouts during fast iteration. Direct `npm run dev` output is faster.
- Cowork can't type into Terminal (it's tier-restricted). Claude Code IS the terminal.
- Image generation costs money (~$0.04/image). The script at `scripts/generate-images.py` is idempotent — it skips images that already exist unless you pass `--force`. Use `--only <substring>` to regenerate one image at a time when refining a prompt.

## Files changed in the last hour of this session

```
src/styles/global.css                              (rewrite — new palette)
src/components/Nav.astro                           (rewrite — logo orb + Watch link)
src/components/Footer.astro                        (rewrite — matching brand, working links)
src/components/VideoCard.astro                     (new)
src/components/EmailSignup.astro                   (new)
src/components/DailyContemplation.astro            (new)
src/data/videos.ts                                 (new)
src/pages/index.astro                              (rewrite — full rebrand)
src/pages/watch.astro                              (new)
src/pages/teachers/index.astro                     (new)
src/pages/texts/index.astro                        (new)
src/pages/about.astro                              (new)
public/images/soul-spirit-self-logo.png            (new — extracted from live site)
```

## How to start with Claude Code

```
cd ~/Documents/soul-spirit-self-handover-bundle/soul-spirit-self
claude
```

Then paste the bug list above (or just point Claude Code at this file). Good luck.
