"""
Soul Spirit Self - Light modernisation pass for archaic English translations.

Used by generate-downloads.py and by Claude Code's text ingest pipeline. The
goal is to make Victorian-era PD translations readable for a contemporary
audience without changing substantive translation choices.

Rules (light only):
  - Pronouns: thou/thee/thy/thine → you/your/yours
  - Verb endings: passeth → passes, hath → has, doth → does, maketh → makes,
    cometh → comes, knoweth → knows, etc.
  - Auxiliaries: didst → did, wouldst → would, couldst → could, shalt → shall
  - Drop "verily" except where it's syntactically load-bearing
  - Drop redundant "do" auxiliaries before main verbs ("do verily declare")
  - Keep all Sanskrit/Pali/Greek/Latin/Hebrew tradition terms intact

NOT in scope:
  - Sentence restructuring
  - Vocabulary modernisation beyond pronouns and verb forms
  - Removing "Behold" or other rhetorical interjections
  - Punctuation reform

Usage:
    from modernise import modernise_text
    cleaned = modernise_text(raw_text)
"""

import re

# Tradition terms that must NEVER be modified by this pass.
# (Not enforced via lookahead -- we just don't have rules that touch them.)
PROTECTED_TERMS = {
    # Sanskrit
    "Atman", "Brahman", "Aum", "Maya", "Jiva", "Vaishvanara", "Taijasa", "Prajna",
    "Turiya", "Akasa", "Prana", "Purusha", "Prakriti", "Dharma", "Karma",
    "Samadhi", "Sruti", "Smriti", "Veda", "Vedanta", "Upanishad", "Sutra",
    "Bhagavan", "Ishvara", "Shakti", "Pushan", "Agni", "Indra", "Mahat",
    "Ahamkara", "Buddhi", "Manas", "Citta", "Sushupti", "Svapna", "Jagrat",
    "Ajativada", "Mumukshutva", "Avidya", "Vidya", "Moksha", "Mukti",
    # Christian/contemplative
    "ousia", "hesychia", "kenosis", "theosis", "agape", "logos", "pneuma",
    "Imago Dei", "Lectio Divina",
}

# Order matters: do longer/more-specific patterns first.
RULES = [
    # ── Auxiliaries and modals ──
    (r'\bdidst\b', 'did'),
    (r'\bDidst\b', 'Did'),
    (r'\bwouldst\b', 'would'),
    (r'\bWouldst\b', 'Would'),
    (r'\bcouldst\b', 'could'),
    (r'\bCouldst\b', 'Could'),
    (r'\bshouldst\b', 'should'),
    (r'\bShouldst\b', 'Should'),
    (r'\bmightst\b', 'might'),
    (r'\bMightst\b', 'Might'),
    (r'\bshalt\b', 'shall'),
    (r'\bShalt\b', 'Shall'),
    (r'\bwilt\b', 'will'),
    (r'\bWilt\b', 'Will'),
    (r'\bart\b(?=\s+(?:thou|you|not))', 'are'),
    (r'\bArt\b(?=\s+(?:thou|you|not))', 'Are'),
    (r'\bwert\b', 'were'),
    (r'\bWert\b', 'Were'),

    # ── Pronouns ──
    (r'\bthou\b', 'you'),
    (r'\bThou\b', 'You'),
    (r'\bthee\b', 'you'),
    (r'\bThee\b', 'You'),
    (r'\bthy\b', 'your'),
    (r'\bThy\b', 'Your'),
    (r'\bthine\b', 'yours'),
    (r'\bThine\b', 'Yours'),
    (r'\bye\b', 'you'),
    (r'\bYe\b', 'You'),

    # ── Verb endings (-eth and -est forms) ──
    # Common irregulars first
    (r'\bhath\b', 'has'),
    (r'\bHath\b', 'Has'),
    (r'\bhast\b', 'have'),
    (r'\bHast\b', 'Have'),
    (r'\bdoth\b', 'does'),
    (r'\bDoth\b', 'Does'),
    (r'\bdost\b', 'do'),
    (r'\bDost\b', 'Do'),
    (r'\bsaith\b', 'says'),
    (r'\bSaith\b', 'Says'),

    # Generic -eth endings: passeth → passes, knoweth → knows, etc.
    # Drop the trailing 'eth' but keep regular -s/-es agreement.
    # Words ending in 'cheth', 'sheth', 'sseth' want -es; others want -s.
    (r'\b(\w+(?:[csx]h|ss))eth\b', r'\1es'),
    (r'\b(\w+)eth\b', r'\1s'),
    (r'\b(\w+(?:[csx]h|ss))Eth\b', r'\1es'),
    (r'\b(\w+)Eth\b', r'\1s'),

    # Generic -est second-person endings: knowest → know, sittest → sit
    # Only triggers when preceded by "thou" (now "you") earlier in the line — but
    # since we already swapped pronouns, we just collapse -est for verbs that
    # commonly take it. Be conservative: only the most common.
    (r'\b(know|see|hear|come|go|live|love|sit|stand|rise|fall|speak|say|do|make|take|give|find|seek|believe|trust|fear|hope)est\b', r'\1'),
    (r'\b(Know|See|Hear|Come|Go|Live|Love|Sit|Stand|Rise|Fall|Speak|Say|Do|Make|Take|Give|Find|Seek|Believe|Trust|Fear|Hope)est\b', r'\1'),

    # ── "verily" — drop unless it lands at the start of a sentence as load-bearing ──
    # Drop mid-sentence "verily" entirely
    (r',\s*verily,?\s+', ', '),
    (r'\s+verily\s+', ' '),
    (r'\bverily\s+', ''),
    (r'\bVerily,\s+', ''),

    # ── Drop empty intensifier "do/did" before bare verb ──
    # "Do thou hear" -> "Hear" -- but this is risky, leave alone for now.

    # ── Tighten punctuation around the substitutions ──
    (r'\s+([,.;:!?])', r'\1'),
    (r'\s{2,}', ' '),
]


def modernise_text(text: str) -> str:
    """Apply the full set of rules to a block of text. Idempotent."""
    for pattern, replacement in RULES:
        text = re.sub(pattern, replacement, text)
    return text.strip()


def modernise_paragraphs(text: str) -> str:
    """Apply line-by-line so blank-line structure is preserved."""
    lines = text.split('\n')
    return '\n'.join(modernise_text(line) if line.strip() else line for line in lines)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            sys.stdout.write(modernise_paragraphs(f.read()))
    else:
        sys.stdout.write(modernise_paragraphs(sys.stdin.read()))
