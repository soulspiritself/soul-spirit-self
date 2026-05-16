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
    headline: 'New research maps the "awe network" in the brain — and what activates it',
    note: 'Scientists at Berkeley have identified a cluster of neural regions that activate during experiences of awe, wonder, and self-transcendence. The findings suggest these states share more neurological common ground than previously thought — with implications for how contemplative practice works at a biological level.',
    source: 'Greater Good Science Center',
    readTime: 4,
    url: 'https://greatergood.berkeley.edu',
    date: '2026-05-15',
  },
  {
    category: 'meditation',
    headline: 'Tibetan monks and the science of lucid dreaming',
    note: 'A practitioner account meets sleep-lab data. What happens when decades of contemplative training enter the dream state — and what researchers found when they looked closely.',
    source: 'Tricycle',
    readTime: 3,
    url: 'https://tricycle.org',
    date: '2026-05-13',
  },
  {
    category: 'wisdom',
    headline: 'The Sufi concept of the heart that listens',
    note: 'In classical Sufi teaching the heart is not a feeling organ but a perceiving one. A close reading of what that distinction means for practice — and for how we understand attention itself.',
    source: 'Sounds True',
    readTime: 4,
    url: 'https://www.soundstrue.com',
    date: '2026-05-11',
  },
  {
    category: 'consciousness',
    headline: 'What NDEs reveal about the edges of identity',
    note: 'Researchers reviewing five hundred accounts find consistent patterns that sit awkwardly alongside standard models of the self. The data raises questions that neither neuroscience nor philosophy has fully answered.',
    source: 'Science and Nonduality',
    readTime: 5,
    url: 'https://www.scienceandnonduality.com',
    date: '2026-05-09',
  },
];

export const categoryLabel: Record<SignalStory['category'], string> = {
  consciousness: 'Consciousness & science',
  meditation: 'Meditation',
  wisdom: 'Wisdom traditions',
};
