# Questions for Andrew

Open questions raised during the Claude Code text-rollout sessions.
Each item is a decision that needs a content judgement before I can
ship the corresponding text. Resolved items move to the bottom.

---

(no open questions — all prior items resolved per Andrew's
2026-04-29 instruction to "take your idea as primary and adjust
it" on outstanding anomalies; recorded below.)

---

## Resolved

### atma-bodha — translator/source mismatch (resolved 2026-04-27)
Use **Charles Johnston 1923**. Original appeared in *The
Theosophical Quarterly* (later collected as "The Awakening to the
Self" in the 1946 volume). Awaiting `cjw.txt.gz` from Andrew to
ingest from the collected printing.

### yoga-vasistha — version + source (resolved 2026-04-27, shipped 2026-04-27)
Use the **abridged Laghu Yoga Vashishta**, Rishi Singh Gherwal
[1930]. Shipped from `yvhf.txt` Andrew provided.

### vivekachudamani — translator (resolved 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive to use my own judgement on
outstanding anomalies. Decision: **Charles Johnston, 1925/1946**,
the same translator chosen for atma-bodha. Both atma-bodha and
vivekachudamani live in Johnston's collected *Crest-Jewel of
Wisdom and other writings of Sankaracharya* — a single
`cjw.txt.gz` from sacred-texts will provide both. Frontmatter on
`src/content/texts/vivekachudamani.md` updated with Johnston
attribution; awaiting source file to ingest.

### yoga-sutras — translator/source (resolved 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive. Decision: **Charles Johnston,
1912**, sacred-texts `/hin/ysp/`. Consistent with Johnston for
atma-bodha and vivekachudamani. PG #2526 hosts the same Johnston
1912 text as a fallback. Frontmatter on
`src/content/texts/yoga-sutras.md` updated; awaiting `ysp.txt.gz`
to ingest.

### dark-night-of-the-soul — translator (resolved 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive. Decision: **David Lewis, 1864**,
the legal-clean strict-PD translation, sourced from archive.org.
The CCEL URL in Cowork's frontmatter actually points at Peers
1934-35 (US copyright until 2030). Frontmatter on
`src/content/texts/dark-night-of-the-soul.md` updated to point at
`archive.org/details/darknightofsoul00john_0` (Lewis 1864), pending
verification of djvu OCR quality on that item.

### interior-castle — translator (resolved 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive. Decision: **Benedictines of
Stanbrook revision, edited by Father Benedict Zimmerman, 1912**,
sacred-texts `/chr/tic/`. David Lewis did not translate Interior
Castle (he did the Life of St. Teresa, 1870). The Stanbrook
revision is the strict-PD English text most readers see. Frontmatter
on `src/content/texts/interior-castle.md` updated; awaiting
`tic.txt.gz` to ingest.

### confessions — frontmatter URL was pointing at wrong CCEL work (resolved 2026-04-27)
Silently fixed during ingest. CCEL hosts both Outler 1955 (in
copyright) and Pusey 1838 (PD) under different URL paths. Pointed
sourceUrl at Pusey.

### Christian devotional Thou/Thee handling (resolved 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive. Decision: **keep modernise.py
default behaviour**, which converts thou/thee/thy → you/your across
the board. Pragmatic reasons: (1) the handoff explicitly mandates
applying modernise.py and not modernising beyond it; (2) consistency
across Sanskrit and Christian texts; (3) the alternative of preserving
Thou for God-addresses requires sentence-level disambiguation that
goes beyond the script's design. Already shipping this way.

### lost-books-of-the-bible — theme-fit (deferred 2026-04-29 by Claude)
Per Andrew's 2026-04-29 directive. Decision: **defer ingest** for
now. The Lost Books of the Bible (sacred-texts `/chr/lbob/`) is
biblical apocrypha — gospels of Nicodemus, Egyptians, Hebrews, etc.
This is biblical-studies content, more historical than contemplative,
and sits oddly next to the contemplative/mystical material that is
the rest of the site. The .txt is downloaded and parked at
`/Users/andrew/Downloads/lbob.txt` if you want to revisit; I'll
process if you confirm it belongs in this library.
