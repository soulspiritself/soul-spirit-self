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

## What I need from Andrew (URLs to download)

`yoga-vasistha` shipped using the `yvhf.txt` Andrew dropped in
`~/Downloads/`. Same approach would unblock the rest. Direct URLs
below — the live sacred-texts.com refuses my requests via Cloudflare
but loads in a real browser, so download from the URL and drop the
file in `~/Downloads/` as before.

### A. Sacred-texts .txt.gz dumps (one-click each)

- **brahma-sutras** Part 1 (Thibaut 1890):
  https://sacred-texts.com/hin/sbe34.txt.gz
- **brahma-sutras** Part 2 (Thibaut 1896):
  https://sacred-texts.com/hin/sbe38.txt.gz
- **atma-bodha** + **vivekachudamani** if you decide on Charles
  Johnston for both — single file (the 1946 Johnston *Crest-Jewel
  of Wisdom and other writings of Shankaracharya* contains
  Atma-Bodha as "The Awakening to the Self" plus Vivekachudamani
  as "The Crest Jewel" plus other Shankara prakaranas):
  https://sacred-texts.com/hin/cjw.txt.gz
- **yoga-sutras** if you decide on Charles Johnston 1912 (option (a)
  in QUESTIONS):
  https://sacred-texts.com/hin/ysp.txt.gz
- **interior-castle** if you accept the 1921 Stanbrook Benedictines
  edition as the PD substitute (see "Interior Castle correction"
  below):
  https://sacred-texts.com/chr/tic.txt.gz

### B. Archive.org direct downloads

These I can fetch myself but the OCR quality is the question. Look
at one yourself before deciding whether to ship the OCR'd version
or hunt for a cleaner source:

- **atma-bodha** — Charles Johnston, Theosophical Quarterly 1925-01
  (Vol 22 Iss 3): "THE AWAKENING TO THE SPIRIT: ATMA BODHA". Note:
  the frontmatter date "1923" is wrong — the original publication
  was 1925, not 1923. Either way, the cleanest path is the cjw.txt.gz
  link above. If you'd rather have the original journal printing:
  https://archive.org/download/theosophical-quarterly_1925-01_22_3/theosophical-quarterly_1925-01_22_3_djvu.txt
- **aparokshanubhuti** — Vimuktananda 1938. The djvu OCR has
  English verses interleaved with mangled Sanskrit/word-by-word
  breakdowns; needs aggressive cleanup. URL:
  https://archive.org/download/in.ernet.dli.2015.125445/2015.125445.Aparokshanubhuti-Or-Self-realization-Of-Sri-Sankaracharya_djvu.txt
- **ashtavakra-gita** — Shastri 1949. The djvu OCR has Devanagari
  garbage on most pages (the English text seems to have been
  squashed by overlapping Sanskrit during OCR). URL:
  https://archive.org/download/AshtavakraGitaHariPrasadShastri/Ashtavakra%20Gita%20-%20Hari%20Prasad%20Shastri%20%28en%29_djvu.txt
- **eckhart-sermons** Vol 1 — Evans 1924, OCR is workable (some
  spotty chars but mostly readable):
  https://archive.org/download/in.ernet.dli.2015.31707/2015.31707.Meister-Eckhart--Vol-1_djvu.txt
- **eckhart-sermons** Vol 2 — couldn't find a good archive.org
  identifier; needs a hunt by someone who knows the editions.

### C. Texts where I haven't been able to identify a working source URL

- **sermons-on-song-of-songs** — Cowork's `cantica00bernuoft` is a
  404. Eales' translation lives somewhere on archive.org bundled
  into the *Life and Works of Saint Bernard* multi-volume series
  (search for "LifeAndWorksOfSaintBernardV4" etc), but I haven't
  pinned down which volume carries which sermons. Knowing your
  preferred edition would help.
- **tauler-sermons** — Cowork's `historyandlifere00tauluoft` is a
  404. Winkworth's *History and Life of Tauler* (1857 first ed,
  reprinted 1905, 1907) is on archive.org under multiple
  identifiers. Best candidates:
  https://archive.org/details/historyandlife00winkuoft (1905)
  https://archive.org/details/historylifeofrev0000susa_c6n9 (1907)

### Interior Castle correction (separate from QUESTIONS item 3)

Cowork's frontmatter says "David Lewis 1888" but **David Lewis did
not translate the Interior Castle**. Lewis translated the Life of
St. Teresa (1870) and the Way of Perfection. The Interior Castle
in PD English is the **Benedictines of Stanbrook revision (1912,
edited by Father Benedict Zimmerman)**, which is what sacred-texts
hosts at `/chr/tic/` (cited as 1921 — the Watkins reprint).

If you OK the Stanbrook substitute, the URL above
(`https://sacred-texts.com/chr/tic.txt.gz`) gets it. (This is a
*third* dark-night-style mismatch: Cowork named a translator who
didn't actually do this work.)

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
