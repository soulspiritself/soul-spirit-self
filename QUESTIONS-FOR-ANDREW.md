# Questions for Andrew

Open questions raised during the Claude Code text-rollout sessions.
Each item is a decision that needs a content judgement before I can
ship the corresponding text. Resolved items move to the bottom.

---

## 1. vivekachudamani — translator attribution wrong

The current frontmatter at `src/content/texts/vivekachudamani.md`
says:
- translator: **Mohini M. Chatterji**, 1932
- sourceUrl: `archive.org/details/crestjewelofwisd00sank`

Two problems:
- That archive.org item returns **404**.
- Mohini Chatterji didn't translate Vivekachudamani. He translated
  the Bhagavad Gita (1887). The 1932 date matches Swami Madhavananda's
  revised edition, not Chatterji.

Real PD options on archive.org:

- **(a)** Charles Johnston — *The Crest-Jewel of Wisdom and other
  writings of Sankaracharya* — first edition 1925 (Quarterly Book
  Department, NY), reprinted 1946 (copyright not renewed → US PD).
  Same translator you picked for atma-bodha. Available at
  `archive.org/details/thecrestjewelofwisdom` and on sacred-texts at
  `/hin/cjw/`.
- **(b)** Swami Madhavananda — *Vivekachudamani of Sri
  Sankaracharya* — first edition 1921 (Advaita Ashrama), revised
  1932. Strict 580-verse rendering plus Sanskrit. Ramakrishna Order
  free-distribution policy (same as the Mandukya Karika source).
  Available at `archive.org/details/vivekachudamanio00sankrich`.

Want me to use (a) Johnston (consistent with your atma-bodha
choice) or (b) Madhavananda (consistent with the Mandukya Karika
source already on the site)?

**Status:** waiting.

---

## 2. yoga-sutras — translator/source mismatch

The current frontmatter at `src/content/texts/yoga-sutras.md` says:
- translator: **James Haughton Woods**, 1914
- sourceUrl: `https://www.gutenberg.org/ebooks/46082`

Two problems:
- PG #46082 is Giovanni Pascoli's *La mirabile visione* (Italian
  Dante commentary), not Woods.
- Woods's *Yoga System of Patanjali* (1914, Harvard Oriental Series
  vol. 17) is **not on Project Gutenberg** at all. It's available
  only as an archive.org scan, and at 380+ pages it's a much heavier
  edition than what we're shipping for the other Upanishads.

PD options:
- **(a)** Charles Johnston, 1912 (Project Gutenberg #2526, also at
  sacred-texts `/hin/ysp/`). Short, clean, 4 books, ~196 sutras.
  Same translator you picked for atma-bodha.
- **(b)** James Haughton Woods, 1914 (archive.org scan only).
  Sutras + Vyasa-bhasya + commentary. Long.

Want (a) Johnston for consistency, or stick with the (b) Woods
choice the frontmatter already names?

**Status:** waiting.

---

## 3. dark-night-of-the-soul — translator/source mismatch

The current frontmatter at `src/content/texts/dark-night-of-the-soul.md`
says:
- translator: **David Lewis**, 1864
- sourceUrl: `https://ccel.org/ccel/john_cross/dark_night/dark_night`

The text actually hosted at that CCEL URL is **E. Allison Peers,
1934–35**. CCEL marks it Public Domain but Peers's translation is
US copyright until 1.1.2030 (95 years from 1934). UK life+70 it's
been PD since 2023 (Peers died 1952). Two paths:

- **(a)** Use Lewis 1864 as the frontmatter currently claims. Lewis
  died 1895; strict PD everywhere. Source it from archive.org.
- **(b)** Accept the Peers edition CCEL hosts. Reads better than
  Lewis but legally weaker (US copyright until 2030 unless we lean
  on CCEL's PD assertion).

Want (a) Lewis (legal-clean) or (b) Peers (better English, accept
CCEL's PD claim with a caveat)?

**Status:** waiting.

---

## 5. Christian devotional texts: should "Thou" be preserved for God?

`modernise.py` converts thou/thee/thy/thine → you/your across the
board. For Sanskrit translations this is straightforwardly a win. For
Christian devotional prose (Augustine's Confessions, Julian's
Revelations, the Cloud of Unknowing) it converts addresses to God
into the conversational "you," which loses the canonical reverential
register. "Great art Thou, O Lord, and greatly to be praised" becomes
"Great art You, O Lord, and greatly to be praised."

The handoff explicitly says to apply modernise.py and not modernise
beyond it, so I'm shipping the Christian texts with thou→you applied
across the board. If you'd prefer Christian texts to preserve Thou
for God specifically (a 1-line tweak to modernise.py: skip the
substitution when the preceding word is in {O, art, dost, didst,
unto, before, in, with, to} or follows certain capitalised vocatives
like "Lord," "God,"), say so and I'll re-process the affected texts.

**Status:** waiting (low-priority — current behaviour ships and is
internally consistent).

---

## 4. confessions — frontmatter URL was pointing at the wrong CCEL work (silently fixed)

CCEL hosts two Augustine "Confessions": `/ccel/augustine/confessions/`
is **Albert C. Outler 1955** (in US copyright); `/ccel/augustine/confess/`
is the **Edward B. Pusey 1838** translation that the frontmatter
claims. I'm changing the `sourceUrl` to point at the right one. No
flag, just recording.

**Status:** resolved silently.

---

## Resolved

### atma-bodha — translator/source mismatch (resolved 2026-04-27)
Use **Charles Johnston 1923**. Original appeared in *The
Theosophical Quarterly*; clean PD scan/transcription on archive.org.
Action: replace the wisdomlib `sourceUrl` and ingest from a
Johnston-attributed archive.org item.

### yoga-vasistha — version + source (resolved 2026-04-27)
Use the **abridged Laghu Yoga Vashishta**, Rishi Singh Gherwal
[1930], from sacred-texts at `/hin/yvhf/`. Page frontmatter to be
updated from "Vihari Lala Mitra 1891 / archive.org" to Gherwal/
sacred-texts. Strict PD (US PD as of 1.1.2026 for 1930 works).
