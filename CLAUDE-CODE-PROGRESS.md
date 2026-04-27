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
- **confessions** — Edward B. Pusey, 1838. Full text (112,554 words
  / ~512 min) ingested from CCEL plain-text cache, modernised,
  downloads built. Frontmatter `sourceUrl` corrected from the
  Outler-1955 URL Cowork had specified to the Pusey edition the
  frontmatter actually claims.
- **theologia-germanica** — Susanna Winkworth, 1854. Full text
  (40,643 words / ~185 min) ingested from CCEL plain-text cache,
  modernised, downloads built.
- **revelations-of-divine-love** — Grace Warrack, 1901. Full text
  (62,698 words / ~285 min) ingested from Project Gutenberg #52958
  plain-text, modernised, downloads built. Sixteen revelations
  across 86 chapters.
- **practice-of-the-presence** — generic PD English (Epworth Press
  Authentic Edition 1932–1948). Full text (11,180 words / ~51 min)
  ingested via CCEL `.epub` → pandoc plain-text, modernised,
  downloads built. Four conversations + fifteen letters.
- **cloud-of-unknowing** — Evelyn Underhill, 1922. Full text (44,111
  words / ~201 min) ingested from sacred-texts via the
  Andrew-provided `cou.txt.gz` dump, modernised, downloads built.
  Underhill's introduction plus all 75 chapters.
- **avadhuta-gita** — Hari Prasad Shastri, 1934 (Shanti Sadan free-
  distribution). Full text (7,730 words / ~35 min) ingested from
  archive.org djvu OCR, modernised, downloads built.
- **tripura-rahasya** — Munagala S. Venkataramiah, 1938 (Sri
  Ramanasramam free-distribution). Full text (74,981 words / ~341
  min) ingested from archive.org djvu OCR, modernised, downloads
  built.

## Flagged

Three decisions still need Andrew's call before I can ship the
corresponding texts. Full context in `QUESTIONS-FOR-ANDREW.md`:

- **vivekachudamani** — Cowork's translator attribution (Mohini
  Chatterji 1932) and `sourceUrl` are both wrong. Two PD candidates
  to choose between (Charles Johnston 1925/1946 vs Swami
  Madhavananda 1921/1932).
- **yoga-sutras** — Cowork's `sourceUrl` (Gutenberg #46082) is an
  Italian Dante book, not Woods. Woods 1914 isn't on Gutenberg at
  all. Choose between Charles Johnston 1912 (clean PG #2526) or
  Woods 1914 (long, archive.org scan).
- **dark-night-of-the-soul** — CCEL URL points at Peers 1934–35 (US
  copyright until 2030) but frontmatter claims Lewis 1864. Choose:
  use Lewis (legal-clean, source from archive.org) or Peers
  (cleaner English, accept CCEL's PD assertion).

Plus one design question (low-priority): whether `modernise.py`
should preserve Thou/Thee/Thy in addresses to God for Christian
devotional texts. Currently shipping with full modernisation per
the handoff's explicit instruction.

## Skipped
(none — texts that are unfinished are either flagged above
awaiting a content judgement, or listed in "Need source data
from Andrew" below.)

## Need source data from Andrew

Three categories of remaining work that I can't unblock myself:

### A. Sacred-texts pages (live site is Cloudflare-gated)

The Wayback mirror works for the sacred-texts index pages but is
unreliable for bulk chapter-page scraping. The cou.txt.gz dump
Andrew provided was perfect — same shape would unblock these:

- **yoga-vasistha** — needs `https://sacred-texts.com/hin/yvhf.txt.gz`
  (Rishi Singh Gherwal 1930, abridged Laghu Yoga Vashishta — your
  resolved choice for this slug).
- **brahma-sutras** — needs both
  `https://sacred-texts.com/hin/sbe34.txt.gz` and
  `https://sacred-texts.com/hin/sbe38.txt.gz` (Thibaut 1890 + 1896).

### B. Archive.org items where the OCR (djvu.txt) is unusable

These items exist on archive.org as scanned PDFs, but the only
plain-text version available is the auto-OCR (`*_djvu.txt`), which
is substantially corrupted (Devanagari interleaved with the
English, mojibake, etc.). To ship these I need a clean
transcription source:

- **aparokshanubhuti** — Vimuktananda 1938 from Advaita Ashrama.
  archive.org item `in.ernet.dli.2015.125445` exists with djvu.txt
  but the English verses are interleaved with mangled OCR'd
  Sanskrit and word-by-word breakdowns. A clean transcription (or
  the EPUB extracted to plain text) would unblock.
- **ashtavakra-gita** — Hari Prasad Shastri 1949. archive.org item
  `AshtavakraGitaHariPrasadShastri` djvu.txt is mostly Devanagari
  OCR garbage even on the English verses.

### C. Texts where the Cowork-supplied source URL is wrong and a clean PD source needs identifying

- **atma-bodha** — Andrew chose Charles Johnston 1923. Johnston's
  Atma-Bodha appeared in The Theosophical Quarterly. archive.org
  has the journal issues (`theosophical-quarterly_1923-*`) — once
  we confirm which issue carries the Atma-Bodha translation we
  can ingest from there. Or use the consolidated archive.org item
  `thecrestjewelofwisdom` (Johnston 1946 reprint) which collects
  Johnston's Shankara translations — confirm whether Atma-Bodha
  is included.
- **sermons-on-song-of-songs** — Eales 1895 from `cantica00bernuoft`
  is a 404. Closest archive.org match `LifeAndWorksOfSaintBernardV4`
  (1889) likely contains Eales' translation but needs verification.
- **eckhart-sermons** — Evans 1924 from `meistereckhart01eckhuoft`
  is a 404. archive.org has `in.ernet.dli.2015.31707` (Evans 1924
  vol 1) but vol 2 needs identifying separately.
- **tauler-sermons** — Winkworth 1857 from `historyandlifere00tauluoft`
  is a 404. Closest matches: `historyandlife00winkuoft` (1905) or
  `historylifeofrev0000susa_c6n9` (1907).
- **interior-castle** — David Lewis 1888 from `interiorcastle00tere`
  is a 404. Lewis's 1888 edition needs an archive.org search by
  someone with patience to scroll past the many newer Peers items.

For category C, if Andrew gives an OK on the suggested
substitute identifiers, I can verify each and ingest in a single
pass.

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
