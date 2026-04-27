# Soul Spirit Self — Project context

This file is the orientation point for any Claude session (Cowork, Code, or Chat) working on this project. Read it first.

## What this is

A static-site reboot of soulspiritself.com built in Astro. It's a contemplative content hub and a portfolio piece for institutional pitches. The brand mirrors the existing soulspiritself.com (deep teal palette, gold accent, "Soul Spirit Self" wide-spaced serif title, "A Journey Within" tagline, the orb logo). The deeper layer is a library of contemplative texts and teachers across the nondual traditions.

## Who Andrew is

A content person, not a developer. He works mainly on content ideation and creation. Treat him accordingly:

- Avoid em dashes in writing (use commas, parentheses, or restructure).
- Be direct. He prefers honest assessment over hedging.
- Don't make him do command-line work unless necessary. If you need a command run, write the exact thing he should paste.
- The voice on the site is concise, contemplative, modern. No academic jargon, no devotional throat-clearing.

## Image generation

- Imagen 4 via google-genai. Model `imagen-4.0-generate-001`.
- API key at `~/Documents/Claude/.env` as `GEMINI_API_KEY` (the script falls back to `GOOGLE_API_KEY` if present).
- Generation script at `scripts/generate-images.py`. Idempotent (skips existing). Use `--force --only <substring>` to regenerate one image.
- Images live in `public/images/`. Filename convention: `tradition-<slug>.jpg`, `text-<slug>.jpg`, `teacher-<slug>.jpg`.
- For real people Imagen often refuses or misfires when given the proper name. Workaround: describe the person generically by appearance, role, era, and ethnicity. Always search the web first for accurate appearance reference before writing the prompt.
- Imagen sometimes adds text or watermarks despite "no text" prompts. If it does, regenerate rather than try to fix in post.

## Site structure

```
src/
├── content/                 ← editable Markdown
│   ├── traditions/          ← 1 file per tradition (Advaita, Christian Mysticism)
│   ├── teachers/            ← 1 file per teacher (21 currently)
│   └── texts/               ← 1 file per text (19 currently)
├── pages/
│   ├── index.astro          ← homepage (logo orb, tagline, featured videos, traditions, daily quote, signup)
│   ├── traditions/          ← traditions index + [slug].astro
│   ├── teachers/            ← teachers index (no individual route yet)
│   ├── texts/               ← texts index + [slug].astro
│   ├── watch.astro          ← /watch video gallery
│   └── about.astro
├── components/              ← Nav, Footer, VideoCard, EmailSignup, DailyContemplation, etc.
├── data/
│   └── videos.ts            ← list of YouTube video IDs (homepage Featured + /watch read from this)
└── styles/global.css        ← brand palette, type, layout helpers (single source of truth)
public/images/               ← all imagery + logo
```

## Brand tokens (defined in `src/styles/global.css`)

| Token | Value | Use |
|---|---|---|
| `--teal-deep` | `#1a4a65` | primary background |
| `--teal-mid` | `#2a6a88` | mid gradient |
| `--teal-light` | `#3278a0` | upper gradient |
| `--accent` | `#c9a96e` | gold (CTAs, eyebrows, accents) |
| `--text` | `#f1ead7` | cream type |
| `--text-muted` | `#c9d6dd` | softer type |
| `--serif` | Cormorant Garamond | display + body serif |
| `--sans` | Inter | UI sans |

## Running locally

```
cd ~/Documents/soul-spirit-self-handover-bundle/soul-spirit-self
npm run dev      # http://localhost:4321
npm run build    # produces /dist
npm run preview  # serves the built site
```

## Email signup

`src/components/EmailSignup.astro` is wired to read `PUBLIC_KIT_FORM_ID` from `.env`. Form action is `#` (no-op) until that variable is set. To activate, drop the Kit form ID into `.env` and restart `npm run dev`.

## Deploy

`netlify.toml` is already correct. Build command `npm run build`, publish directory `dist`. Connect the GitHub repo to Netlify, point `soulspiritself.com` at the new site, and every `git push` triggers a redeploy.

## What's done

- Advaita Vedanta tradition: 1 tradition page, 7 teachers, 9 texts, all imagery
- Christian Mysticism tradition: 1 tradition page, 14 teachers (8 full, 6 biographical-only), 10 texts, all imagery
- Brand refresh to mirror the existing soulspiritself.com
- /watch page with the existing site's 9 featured YouTube videos
- Daily contemplation card on homepage (currently a single Mooji quote)
- Email signup component (Kit-ready, awaiting form ID)
- /teachers/, /texts/, /about/ index pages
- 42 Imagen 4 images generated and QA'd

## What's open / open decisions

- Buddhist Nonduality, Sufism, Taoism, Modern Nonduality, Kashmir Shaivism: not yet populated.
- Individual teacher pages (`/teachers/<slug>/`) don't have routes yet. Currently teachers render only as cards on tradition pages and on the teachers index.
- Daily Contemplation rotates through one quote. Could become a content collection of many quotes with random or daily rotation.
- Whether to add Sanskrit/original-language toggles on text pages.
- Whether to add ElevenLabs audio narration for texts.
- Translation question for the Rhineland women mystics, Kashmir Shaivism, Inchagiri (no PD English exists for some major works).

## Working agreement

- Use TodoWrite (or whatever the equivalent is in your mode) for non-trivial work.
- Verify build before declaring a task done. `npm run build` must pass.
- After image generation, do a QA pass and regenerate any with text artifacts, watermarks, or wildly off-brief output.
- When in doubt about a content decision, ask Andrew rather than guess.
- Read `HANDOVER.md` for the strategic context, `COWORK-HANDOFF.md` for the most recent session's tactical notes.
