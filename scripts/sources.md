# Source index for the 21 outstanding texts

Pre-flight reconnaissance, built 2026-04-27 by Claude Code session.

Method:
- Pulled the four sacred-texts.com index pages (`/hin/`, `/chr/`, `/isl/`,
  `/bud/`, `/tao/`) via the Wayback Machine (the live site is gated by
  Cloudflare and refused both WebFetch and curl). Cross-checked each
  candidate edition's title-page metadata.
- Compared findings to the translator/source already encoded in each
  text's `src/content/texts/<slug>.md` frontmatter (Cowork's earlier
  curation pass).
- Confidence column is a judgement on whether the named source can be
  ingested cleanly without further decisions:
  - `high` — source confirmed, translator/year/PD-status verified, clean
    HTML or text expected from the URL on file.
  - `medium` — source confirmed and PD/free, but ingest may need light
    munging (multi-volume archive.org sets, OCR transcription quality
    unverified, very long works).
  - `flagged` — there is a question that needs Andrew's call before I
    proceed (see QUESTIONS-FOR-ANDREW.md).

## Advaita Vedanta (11)

| slug | source URL (frontmatter) | translator | year | platform | confidence |
|---|---|---|---|---|---|
| vivekachudamani | https://archive.org/details/crestjewelofwisd00sank | Mohini M. Chatterji | 1932 | Internet Archive | medium |
| atma-bodha | https://www.wisdomlib.org/hinduism/book/atma-bodha | Charles Johnston (claimed) | 1923 | wisdomlib | flagged |
| aparokshanubhuti | https://archive.org/details/aparokshanubhuti | Swami Vimuktananda | 1938 | Internet Archive | medium |
| yoga-vasistha | https://archive.org/details/YogaVasishthaMaharamayana | Vihari Lala Mitra | 1891 | Internet Archive | flagged |
| ashtavakra-gita | https://archive.org/details/AshtavakraGitaHariPrasadShastri | Hari Prasad Shastri | 1949 | Internet Archive | medium |
| avadhuta-gita | https://archive.org/details/AvadhutGitaHariPrasadShastri | Hari Prasad Shastri | 1934 | Internet Archive | medium |
| tripura-rahasya | https://archive.org/details/tripura-rahasya-eng | M. S. Venkataramiah | 1938 | Internet Archive | medium |
| yoga-sutras | https://www.gutenberg.org/ebooks/46082 | James Haughton Woods | 1914 | Project Gutenberg | high |
| katha-upanishad | https://sacred-texts.com/hin/sbe15/ | Friedrich Max Müller | 1884 | Sacred Texts (SBE 15) | high |
| mundaka-upanishad | https://sacred-texts.com/hin/sbe15/ | Friedrich Max Müller | 1884 | Sacred Texts (SBE 15) | high |
| brahma-sutras | https://sacred-texts.com/hin/sbe34/ + sbe38/ | George Thibaut | 1890, 1896 | Sacred Texts (SBE 34, 38) | high |

## Christian Mysticism (10)

| slug | source URL (frontmatter) | translator | year | platform | confidence |
|---|---|---|---|---|---|
| confessions | https://ccel.org/ccel/augustine/confessions/confessions | Edward Bouverie Pusey | 1838 | CCEL | high |
| sermons-on-song-of-songs | https://archive.org/details/cantica00bernuoft | Samuel J. Eales | 1895 | Internet Archive | medium |
| eckhart-sermons | https://archive.org/details/meistereckhart01eckhuoft | C. de B. Evans | 1924 | Internet Archive | medium |
| theologia-germanica | https://ccel.org/ccel/anonymous/theologia/theologia | Susanna Winkworth | 1854 | CCEL | high |
| tauler-sermons | https://archive.org/details/historyandlifere00tauluoft | Susanna Winkworth | 1857 | Internet Archive | medium |
| revelations-of-divine-love | https://www.gutenberg.org/ebooks/52958 | Grace Warrack | 1901 | Project Gutenberg | high |
| cloud-of-unknowing | https://sacred-texts.com/chr/cou/index.htm | Evelyn Underhill | 1922 | Sacred Texts | high |
| dark-night-of-the-soul | https://ccel.org/ccel/john_cross/dark_night/dark_night | David Lewis | 1864 | CCEL | high |
| interior-castle | https://archive.org/details/interiorcastle00tere | David Lewis | 1888 | Internet Archive | medium |
| practice-of-the-presence | https://ccel.org/ccel/lawrence/practice/practice | Various early English (PD) | 1724 | CCEL | medium |

## Sacred-texts cross-check

What the sacred-texts indexes actually offer for the 21 (verified via
title-page metadata):

- **vivekachudamani** — `/hin/cjw/` is Charles Johnston [1946, copyright
  not renewed]. Different translator from Cowork's choice
  (Chatterji 1932). Both PD. Cowork's choice is fine; sacred-texts is a
  fallback.
- **atma-bodha** — `/hin/wos/` ("Select Works of Sri Sankaracharya",
  S. Venkataramanan 1921) contains Atma-Bodha alongside other Shankara
  prakaranas. Strict PD. Likely the correct PD substitute for the
  flagged Johnston-on-wisdomlib mismatch (see QUESTIONS).
- **aparokshanubhuti** — not present on sacred-texts. Cowork's
  archive.org Vimuktananda 1938 is the standard choice.
- **yoga-vasistha** — `/hin/yvhf/` is Rishi Singh Gherwal's 1930
  *Laghu* (abridged) Yoga Vashishta, NOT the full Mitra. Cowork's
  archive.org Mitra 1891 is correct for the full work but it is a
  4-volume scan set; pipeline ingest will need a known-good text
  source. Flagged.
- **ashtavakra-gita / avadhuta-gita / tripura-rahasya** — not on
  sacred-texts. Cowork's archive.org choices stand.
- **yoga-sutras** — Project Gutenberg #46082 (Woods 1914) is correct
  for Cowork's choice. Sacred-texts also has Charles Johnston [1912]
  at `/hin/ysp/` as a clean alternative; either is fine.
- **katha-upanishad / mundaka-upanishad** — both inside SBE 15
  (Müller 1884) at `/hin/sbe15/`.
- **brahma-sutras** — Thibaut SBE 34 [1890] + SBE 38 [1896] split
  across `/hin/sbe34/` and `/hin/sbe38/`. The Ramanuja edition (SBE
  48) at `/hin/sbe48/` is also present but not what Cowork specified.

- **confessions** — sacred-texts `/chr/augconf/` is the same Pusey
  translation (printing dated 1909–14). CCEL link in frontmatter is
  fine; sacred-texts is a fallback.
- **cloud-of-unknowing** — `/chr/cou/` is Underhill [1922]. Matches.
- **interior-castle** — sacred-texts `/chr/tic/` is an unattributed
  1921 edition (almost certainly the Benedictines of Stanbrook
  revision, not Lewis 1888 and not Peers 1946). Cowork's choice of
  Lewis 1888 from Internet Archive is the older PD edition and
  matches what's in frontmatter. Stands.
- **sermons-on-song-of-songs / eckhart-sermons / tauler-sermons /
  revelations-of-divine-love / dark-night-of-the-soul / theologia-
  germanica / practice-of-the-presence** — none on sacred-texts. The
  CCEL/archive.org/Gutenberg sources Cowork chose are the right ones.

## Pipeline order (proposed)

Process in order of cleanliness and decisiveness, leaving the flagged
two until Andrew has weighed in:

1. **katha-upanishad** — sacred-texts SBE 15, single sub-page, ~119 verses.
2. **mundaka-upanishad** — sacred-texts SBE 15, single sub-page, ~64 verses.
3. **vivekachudamani** — archive.org Chatterji 1932, ~580 verses.
4. **yoga-sutras** — Project Gutenberg #46082 (HTML or .txt clean), 196 sutras + Woods commentary (potentially huge — may decide commentary out of scope).
5. **cloud-of-unknowing** — sacred-texts `/chr/cou/`, 75 chapters.
6. **brahma-sutras** — sacred-texts SBE 34 + 38, 555 sutras + Shankara's bhasya across two volumes (very long).
7. **revelations-of-divine-love** — Gutenberg #52958.
8. **theologia-germanica** — CCEL.
9. **dark-night-of-the-soul** — CCEL.
10. **confessions** — CCEL, 13 books.
11. **practice-of-the-presence** — CCEL, short.
12. **aparokshanubhuti / ashtavakra-gita / avadhuta-gita / tripura-rahasya** — archive.org transcription quality to be checked when reached.
13. **sermons-on-song-of-songs / eckhart-sermons / tauler-sermons / interior-castle** — archive.org scan sets, ingest path TBD per text.
14. **yoga-vasistha** — only after Andrew's call (size + source).
15. **atma-bodha** — only after Andrew's call (translator mismatch).
