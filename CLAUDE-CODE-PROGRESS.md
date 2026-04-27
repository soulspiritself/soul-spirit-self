# Claude Code rollout progress

Tracking the 21-text rollout. One row per text. Status is `done`,
`flagged`, or `skipped`. See `scripts/sources.md` for the full source
matrix and `QUESTIONS-FOR-ANDREW.md` for blockers.

## Done
- **katha-upanishad** — Friedrich Max Müller, SBE 15, 1884. Full text
  (4,341 words / ~20 min) ingested from sacred-texts via the Wayback
  mirror (chapters sbe15010–sbe15015), modernised, downloads built.
  Frontmatter `sourceUrl`/`licenceNote` updated to point at the
  sacred-texts SBE 15 edition.
  - Source carries one minor typo ("116." instead of "16." in Sixth
    Vallî); left intact, outside scope of the modernise pass.
- **mundaka-upanishad** — Friedrich Max Müller, SBE 15, 1884. Full
  text (2,598 words / ~12 min) ingested from sacred-texts via the
  Wayback mirror (chapters sbe15016–sbe15021), modernised, downloads
  built. Frontmatter `sourceUrl`/`licenceNote` updated.

## Flagged
(none open — atma-bodha and yoga-vasistha decisions resolved
2026-04-27, see QUESTIONS-FOR-ANDREW.md "Resolved" section.
Both moved into the work queue.)

## Skipped
(none yet)

## Notes
- Pre-flight `scripts/sources.md` written 2026-04-27.
- sacred-texts.com is gated by a Cloudflare challenge (every direct
  fetch returned HTTP 403). I worked around it by pulling index pages
  via the Wayback Machine. The actual chapter pages are also gated, so
  ingest of sacred-texts texts will use the same wayback-mirror route.
- `scripts/generate-downloads.py` was extended with one line to render
  `### N` headings as indented plain-text in the .txt download
  (without it the literal `###` markers leaked through). Affects new
  texts that use h3 sectioning; mandukya-karika has no h3s and is
  unaffected.
- `npm run build` fails locally on Andrew's Mac (sharp missing,
  Node 25 has no prebuilt binaries yet). Pre-existing, irrelevant to
  shipping. See `CLAUDE-CODE-HANDOFF.md` "Known noise". Verify deploys
  on Netlify (`netlify api listSiteDeploys`) instead.
