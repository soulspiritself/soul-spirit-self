// The Signal — curated story data
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
    headline: 'What awe looks like in the brain',
    note: 'When researchers used fMRI to scan people watching awe-inducing nature videos, activity in the default mode network (the region most active during self-referential thinking) quieted. A small finding with a large implication for why moments of awe leave us feeling less self-centred.',
    source: 'Greater Good Science Center',
    readTime: 5,
    url: 'https://greatergood.berkeley.edu/article/item/what_awe_looks_like_in_the_brain',
    date: '2026-05-15',
  },
  {
    category: 'meditation',
    headline: 'Tibetan dream yoga: waking up inside the dream',
    note: 'Tibetan practitioners have used lucidity in dreams as serious spiritual training for a thousand years, treating the dream state as preparation for the dissolution of self at death. A grounded primer on the lineage, the technique, and why some teachers consider dream practice more potent than waking practice.',
    source: 'Tricycle',
    readTime: 6,
    url: 'https://tricycle.org/magazine/tibetan-dream-yoga/',
    date: '2026-05-13',
  },
  {
    category: 'wisdom',
    headline: 'The heart as an organ of perception',
    note: 'In Sufi understanding the heart is not a feeling organ but a perceiving one, a place that knows without thinking. A short clear reading on the heart as the spiritual organ through which the Divine Essence is directly experienced.',
    source: 'The Golden Sufi Center',
    readTime: 4,
    url: 'https://goldensufi.org/article/lover-and-beloved/',
    date: '2026-05-11',
  },
  {
    category: 'consciousness',
    headline: 'Near-death experiences and the case against the materialist self',
    note: 'Marjorie Woollacott takes the standard sceptical critiques of NDE research head-on. The patterns in the data, drawn from thousands of accounts, sit awkwardly inside any purely materialist account of mind.',
    source: 'Science and Nonduality',
    readTime: 7,
    url: 'https://scienceandnonduality.com/article/near-death-experiences-are-real-a-rebuttal/',
    date: '2026-05-09',
  },
];

export const categoryLabel: Record<SignalStory['category'], string> = {
  consciousness: 'Consciousness & science',
  meditation: 'Meditation',
  wisdom: 'Wisdom traditions',
};
