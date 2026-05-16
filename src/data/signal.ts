// The Signal — curated story data
// Editorial focus: nonduality, consciousness science, idealism, simulation theory,
// the world as appearance in awareness, the traditions that have been pointing at this for millennia.
// Add new stories at the top of the array. The homepage shows the first 4.
// category: 'consciousness' | 'meditation' | 'wisdom'

export interface SignalStory {
  category: 'consciousness' | 'meditation' | 'wisdom';
  headline: string;
  note: string;
  source: string;
  readTime: number; // minutes
  url: string;
  date: string; // ISO date string, e.g. '2026-05-16'
}

export const signalStories: SignalStory[] = [
  {
    category: 'consciousness',
    headline: 'Analytic idealism: a serious case that the world is mental',
    note: 'Bernardo Kastrup argues that universal consciousness is all there ultimately is, and what we call physical objects are appearances of mental activity. The piece sets out how dissociation, the same phenomenon clinicians observe in DID, can explain why each of us experiences ourselves as a separate self inside a shared world.',
    source: 'Essentia Foundation',
    readTime: 9,
    url: 'https://www.essentiafoundation.org/analytic-idealism-and-the-possibility-of-a-meta-conscious-cosmic-mind/reading/',
    date: '2026-05-16',
  },
  {
    category: 'consciousness',
    headline: 'Reality is a user interface',
    note: 'Cognitive scientist Donald Hoffman argues that evolution shaped our senses to hide reality, not reveal it. What we see is a desktop of icons, useful for surviving but no more "true" than the trash can on your laptop is a real receptacle.',
    source: 'Science and Nonduality',
    readTime: 6,
    url: 'https://scienceandnonduality.com/article/reality-is-a-user-interface-donald-hoffman/',
    date: '2026-05-15',
  },
  {
    category: 'consciousness',
    headline: 'Quantum fields are consciousness',
    note: 'Federico Faggin, the engineer who invented the microprocessor, now argues that consciousness is not produced by the brain but is the substance of quantum fields themselves. Each quantum state is unique and uncopiable, matching the privacy of subjective experience in a way classical physics cannot.',
    source: 'Essentia Foundation',
    readTime: 8,
    url: 'https://www.essentiafoundation.org/quantum-fields-are-consciousness-a-groundbreaking-new-theory-by-the-inventor-of-the-microprocessor/seeing/',
    date: '2026-05-14',
  },
  {
    category: 'wisdom',
    headline: 'The world should be considered like a dream',
    note: 'Ramana Maharshi on why Advaita treats waking experience as continuous with the dream state, not opposed to it. Both are appearances in awareness, and recognising that is the beginning of self-enquiry.',
    source: 'Tom Das',
    readTime: 5,
    url: 'https://tomdas.com/2020/03/25/ramana-maharshi-the-world-should-be-considered-like-a-dream/',
    date: '2026-05-13',
  },
  {
    category: 'consciousness',
    headline: 'It from bit: the universe as a participatory phenomenon',
    note: 'Maria Popova on the physicist John Archibald Wheeler, who argued that information, not matter, is the bedrock of reality, and that observation is not a passive recording of what is but part of what brings it into being.',
    source: 'The Marginalian',
    readTime: 7,
    url: 'https://www.themarginalian.org/2016/09/02/it-from-bit-wheeler/',
    date: '2026-05-12',
  },
  {
    category: 'wisdom',
    headline: 'An introduction to non-duality',
    note: 'Rupert Spira on why the world’s contemplative traditions point at one shared insight: that awareness, not the body or mind, is what we essentially are, and that the apparent separation between self and world is a misreading of experience.',
    source: 'Rupert Spira',
    readTime: 8,
    url: 'https://rupertspira.com/non-duality/blog/article/an_introduction_to_non-duality',
    date: '2026-05-11',
  },
  {
    category: 'consciousness',
    headline: 'Simulation theory: the mystics got there first',
    note: 'A look at the growing scholarly conversation linking the simulation hypothesis to ideas long carried in Hindu, Buddhist, and gnostic traditions. Whether or not the universe is computational, the suspicion that what we take for solid reality is something subtler is older than physics.',
    source: 'Religion News Service',
    readTime: 6,
    url: 'https://religionnews.com/2025/11/17/simulation-theory-brings-an-ai-twist-out-of-the-matrix-to-ideas-mystics-and-religious-scholars-have-voiced-for-centuries/',
    date: '2026-05-10',
  },
  {
    category: 'consciousness',
    headline: 'The hard problem of consciousness is a distraction from the real one',
    note: 'An Aeon essay arguing that the standard framing (how does matter produce experience?) is upside down. Take consciousness as the ground rather than the puzzle, and the philosophical knot loosens. Panpsychism and idealism move from fringe to serious alternative.',
    source: 'Aeon',
    readTime: 11,
    url: 'https://aeon.co/essays/the-hard-problem-of-consciousness-is-a-distraction-from-the-real-one',
    date: '2026-05-09',
  },
  {
    category: 'consciousness',
    headline: 'What awe looks like in the brain',
    note: 'When researchers used fMRI to scan people watching awe-inducing nature videos, activity in the default mode network (the region most active during self-referential thinking) quieted. A small finding with a large implication for why moments of awe leave us feeling less self-centred.',
    source: 'Greater Good Science Center',
    readTime: 5,
    url: 'https://greatergood.berkeley.edu/article/item/what_awe_looks_like_in_the_brain',
    date: '2026-05-08',
  },
  {
    category: 'meditation',
    headline: 'Tibetan dream yoga: waking up inside the dream',
    note: 'Tibetan practitioners have used lucidity in dreams as serious spiritual training for a thousand years, treating the dream state as preparation for the dissolution of self at death. A grounded primer on the lineage, the technique, and why some teachers consider dream practice more potent than waking practice.',
    source: 'Tricycle',
    readTime: 6,
    url: 'https://tricycle.org/magazine/tibetan-dream-yoga/',
    date: '2026-05-07',
  },
  {
    category: 'wisdom',
    headline: 'The heart as an organ of perception',
    note: 'In Sufi understanding the heart is not a feeling organ but a perceiving one, a place that knows without thinking. A short, clear reading on the heart as the spiritual organ through which the Divine Essence is directly experienced.',
    source: 'The Golden Sufi Center',
    readTime: 4,
    url: 'https://goldensufi.org/article/lover-and-beloved/',
    date: '2026-05-06',
  },
  {
    category: 'consciousness',
    headline: 'Near-death experiences and the case against the materialist self',
    note: 'Marjorie Woollacott takes the standard sceptical critiques of NDE research head-on. The patterns in the data, drawn from thousands of accounts, sit awkwardly inside any purely materialist account of mind.',
    source: 'Science and Nonduality',
    readTime: 7,
    url: 'https://scienceandnonduality.com/article/near-death-experiences-are-real-a-rebuttal/',
    date: '2026-05-05',
  },
];

export const categoryLabel: Record<SignalStory['category'], string> = {
  consciousness: 'Consciousness & science',
  meditation: 'Meditation',
  wisdom: 'Wisdom traditions',
};
