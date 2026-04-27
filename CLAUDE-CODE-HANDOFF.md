# Claude Code handoff — text library rollout

This document briefs Claude Code (running locally on Andrew's Mac) on the work
to populate the remaining 21 contemplative texts at the new "curated preview
+ downloadable full text" standard. Read it before doing anything else.

## Context (read once, then orient yourself in the codebase)

Soul Spirit Self is a static Astro site Andrew (a content person, not a
developer) is using as both a contemplative library and a portfolio piece.
Three texts already meet the new standard, set up in a long Cowork session:

- **Mandukya Upanishad** — 12 mantras, full text on page, downloads ready
- **Isha Upanishad** — 18 verses, full text on page, downloads ready
- **Mandukya Karika** — 215 verses; page shows 10 curated verses; full work
  in `public/downloads/mandukya-karika.{txt,pdf,epub}`

The pattern: the page MD shows a tight framing essay plus ~10 curated
evocative verses (Andrew picks these or Cowork does). The downloadable
files contain the **full** text. Word count and reading time show in the
sidebar so visitors know the scale before downloading.

The deploy chain is live: GitHub repo `soulspiritself/soul-spirit-self`,
Netlify project `scintillating-rabanadas-15dbed` (site ID
`d7cea993-41f5-4749-a979-164ce9b1b248`), domain `soulspiritself.com`.
Push to main on this Mac → Netlify rebuilds → site updates within ~60s.

`gh auth setup-git` is configured. `NETLIFY_AUTH_TOKEN` is in `~/.zshrc`.
`pandoc`, `weasyprint`, `python markdown/yaml/genai` are all installed.

## Your job

Mechanical pipeline work, scaling the pattern to the remaining 21 texts.
For each one:

1. Find a clean PD digital edition. Default first stop:
   **https://sacred-texts.com** — it only carries PD material across
   `/hin/`, `/chr/`, `/isl/`, `/bud/`, `/tao/`. If sacred-texts has it,
   use it. If not, try Project Gutenberg, Wikisource, archive.org. Avoid
   OCR'd image-scan editions if a clean transcription exists anywhere.
2. Fetch the full text. Save to `scripts/full-texts/<slug>.md` with the
   same frontmatter shape as `scripts/full-texts/mandukya-karika.md`
   (use that file as the template). The body should be the **complete**
   text with section/chapter headings, faithful to the source.
3. Apply the modernisation pass. Use `scripts/modernise.py`:
   `python3 -c "from modernise import modernise_paragraphs as m; ..."`.
   This handles thou/thee/thy/thine, verb-form -eth/-est endings,
   archaic auxiliaries, and drops "verily". Do not modernise beyond
   what that module does. Substantive translation choices stay.
4. Update the page MD at `src/content/texts/<slug>.md` so its frontmatter
   has the right `translator`, `translationYear`, `sourceUrl`,
   `sourcePlatform`, `licence`, `licenceNote`. **Do NOT trim the page
   body to a curated preview** — that's a content judgement, not your
   job. Leave the body as-is for now (or with a single placeholder
   line saying "Cowork to curate verses next session").
5. Run `python3 scripts/generate-downloads.py <slug> --source-md
   scripts/full-texts/<slug>.md`. This produces the three download
   files and injects `downloadTxt`, `downloadPdf`, `downloadEpub`,
   `wordCount`, `readingTimeMinutes` into the page MD frontmatter.
6. Commit with a clear message referencing the slug and translator.
   `git push origin main`. Watch the Netlify deploy succeed before
   moving to the next text. (Use the Netlify MCP or the `netlify api
   listSiteDeploys` CLI command.)

Then track progress in `CLAUDE-CODE-PROGRESS.md` (create if absent) so
the next session can pick up where you left off. One row per text, with
status `done` / `flagged` / `skipped`.

## What you do NOT do

- **Do NOT write framing essays or curate the 10-verse on-page
  selection.** That's content judgement reserved for Andrew or Cowork.
  Leave the page body untouched (or with the placeholder noted above)
  and ship the downloads + frontmatter only.
- **Do NOT modernise beyond `scripts/modernise.py`.** No paraphrasing,
  no sentence restructuring, no vocabulary swaps. The point of this
  pipeline is consistency, not your taste.
- **Do NOT make licensing calls when the source is ambiguous.** If a
  text's translator status is unclear (e.g. between PD and freely-
  distributable), flag it in the progress file with what you found
  and what the question is, and move on. Never silently push a text
  whose licensing you're unsure of.
- **Do NOT generate fresh translations.** If no clean PD or freely-
  distributable English translation exists, mark the text as flagged
  and move on. There are 24 texts to populate; one being deferred is
  fine.
- **Do NOT delete or rename existing image files in `public/images/`.**
- **Do NOT touch the deploy pipeline, Netlify config, GitHub settings,
  or anything in `scripts/full-texts/mandukya-karika.md`.**

## Pre-flight: build the source index FIRST

Before extracting any text, do this once:

1. Fetch the index pages of `https://sacred-texts.com/hin/index.htm`,
   `/chr/index.htm`, `/isl/index.htm`, `/bud/index.htm`,
   `/tao/index.htm`. Search-and-grep for each of the 21 outstanding
   text slugs.
2. Build a table at `scripts/sources.md` with one row per outstanding
   text: slug | best PD source URL | translator | year | platform |
   confidence (`high` | `medium` | `unknown`).
3. Print the table. Andrew or future-Cowork will read it as a sanity
   check before you start extracting.

This single preflight saves cycles by eliminating the "search per text"
loop and surfaces missing-source issues in 10 minutes instead of 5
hours.

## Outstanding texts (21)

### Advaita Vedanta (11)
- vivekachudamani — Shankara, ~581 verses (likely sacred-texts has Madhavananda PD)
- atma-bodha — Shankara, 68 verses (frontmatter currently mis-attributes Charles Johnston 1923 to a Chinmayananda source — verify and fix)
- aparokshanubhuti — Shankara, 144 verses
- yoga-vasistha — ~32,000 verses, Mitra 1891 (huge — page = curated preview, downloads = full)
- ashtavakra-gita — 298 verses (Hari Prasad Shastri 1949 under Shanti Sadan free-distribution)
- avadhuta-gita — 192 verses (Shastri 1934, same policy)
- tripura-rahasya — Venkataramiah 1938 (Sri Ramanasramam free-distribution)
- yoga-sutras — Patanjali, Woods 1914 (Project Gutenberg has it clean)
- katha-upanishad — 119 verses, Müller SBE 15
- mundaka-upanishad — 64 mantras, Müller SBE 15
- brahma-sutras — 555 sutras + Shankara's bhasya, Thibaut SBE 34 + 38

### Christian Mysticism (10)
- confessions — Augustine, Pusey 1838
- sermons-on-song-of-songs — Bernard, Eales/Mabillon
- eckhart-sermons — Pfeiffer
- theologia-germanica — Winkworth
- tauler-sermons — Susanna Winkworth
- revelations-of-divine-love — Julian of Norwich, Warrack 1901
- cloud-of-unknowing — Underhill 1922
- dark-night-of-the-soul — John of the Cross, Lewis or Peers
- interior-castle — Teresa of Avila, Peers
- practice-of-the-presence — Brother Lawrence (multiple PD editions)

## Flag-and-skip examples

If you hit any of these situations, write a row in
`CLAUDE-CODE-PROGRESS.md` with status `flagged` and the reason, then
move on:

- The text on sacred-texts is a Sanskrit-only edition (no English).
- The English translation on sacred-texts predates 1900 but is so
  archaic that even the modernise.py pass leaves the result hard to
  read. (Andrew has explicitly said light modernisation is enough for
  these; if you think a text needs deep restructuring, flag it.)
- Multiple translators are available and you can't tell which Andrew
  prefers.
- The source URL works but returns garbage HTML / OCR-fragmented text.
- The book is multiple volumes and you've completed volume 1 but the
  others are missing or significantly different translators.

## Output file

Maintain `CLAUDE-CODE-PROGRESS.md` at the repo root with this shape:

```markdown
# Claude Code rollout progress

## Done
- mundaka-upanishad — Müller SBE 15, full text + downloads, commit abc1234
- katha-upanishad — Müller SBE 15, full text + downloads, commit def5678

## Flagged
- atma-bodha — frontmatter says Johnston 1923 but linked source is
  Chinmayananda (still under copyright). Need Andrew or Cowork to
  pick a PD translator (Mohini Chatterji 1893 is candidate).
- ...

## Skipped
- (none yet)
```

This is what the next Cowork session picks up to do the curation pass.

## Final reminders

Andrew is a content person, not a developer. If something requires his
input, write the question to `QUESTIONS-FOR-ANDREW.md` at the repo root
in plain English with the choice clearly framed. Don't expect him to
read code or run commands.

Don't invent. Don't guess. When the source is unclear, flag.

Let's go.

## Known noise (do NOT pause on these)

- **`npm run build` fails locally on Andrew's Mac** with `Rollup
  failed to resolve import "sharp"`. This is pre-existing and
  irrelevant to shipping. Andrew's Mac runs Node 25; sharp doesn't
  yet have prebuilt binaries for it. Netlify is pinned to Node 22 in
  `netlify.toml`, where sharp installs cleanly and the build succeeds.
  Do not try to install sharp locally, do not block on the local
  build, do not paste the error to Andrew. Commit, push, and verify
  via `netlify api listSiteDeploys` instead.
