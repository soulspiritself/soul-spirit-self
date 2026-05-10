// Daily contemplation quotes.
// One quote per day of the year, cycled by day-of-year so it rotates
// deterministically (same quote for everyone on the same day).
//
// All quotes here are either public-domain (pre-1929 sources or translations)
// or short widely-attributed sayings from teachers represented elsewhere on
// the site. Keep each entry to a single short sentence to preserve the
// contemplative single-line format of the card.

export interface Contemplation {
  quote: string;
  author: string;
  source?: string;
}

export const contemplations: Contemplation[] = [
  {
    quote: 'To be here, fully here, in this timeless moment, is the ultimate freedom.',
    author: 'Mooji',
    source: 'Dawn Rising',
  },
  {
    quote: 'Your own Self-realization is the greatest service you can render the world.',
    author: 'Ramana Maharshi',
  },
  {
    quote: 'All shall be well, and all shall be well, and all manner of thing shall be well.',
    author: 'Julian of Norwich',
    source: 'Revelations of Divine Love',
  },
  {
    quote: 'Thou hast made us for thyself, and our heart is restless until it find rest in thee.',
    author: 'Augustine of Hippo',
    source: 'Confessions',
  },
  {
    quote: 'The eye through which I see God is the same eye through which God sees me.',
    author: 'Meister Eckhart',
  },
  {
    quote: 'Let nothing disturb thee. Let nothing affright thee. All things are passing.',
    author: 'Teresa of Avila',
  },
  {
    quote: 'Lift up thine heart unto God with a meek stirring of love.',
    author: 'The Cloud of Unknowing',
  },
  {
    quote: 'In the silence of the heart, God speaks.',
    author: 'A common contemplative saying',
  },
  {
    quote: 'The wave is the same as the ocean, though it is not the whole ocean.',
    author: 'Ramakrishna',
  },
  {
    quote: 'You are the sky. Everything else is just the weather.',
    author: 'A modern contemplative saying',
  },
  {
    quote: 'Wisdom tells me I am nothing. Love tells me I am everything. Between the two my life flows.',
    author: 'Nisargadatta Maharaj',
  },
  {
    quote: 'I make of all the actions of my life one continual conversation with God.',
    author: 'Brother Lawrence',
    source: 'The Practice of the Presence of God',
  },
  {
    quote: 'When the mind is silent, the world becomes transparent.',
    author: 'A contemplative saying',
  },
  {
    quote: 'You have the right to work, but never to the fruit of work.',
    author: 'Bhagavad Gita',
  },
  {
    quote: 'Be still, and know that I am God.',
    author: 'Psalm 46',
  },
  {
    quote: 'The Tao that can be spoken is not the eternal Tao.',
    author: 'Lao Tzu',
    source: 'Tao Te Ching',
  },
  {
    quote: 'You yourself are the eternal substance of which everything seeks to drink.',
    author: 'Hadewijch',
  },
  {
    quote: 'There is a candle in your heart, ready to be kindled.',
    author: 'Rumi',
  },
  {
    quote: 'The teacher who desires to follow the contemplative path will give the soul milk to drink, not meat to eat.',
    author: 'Bernard of Clairvaux',
    source: 'Sermons on the Song of Songs',
  },
  {
    quote: 'Soul, take leave of yourself. The simple soul has nothing more to ask of itself.',
    author: 'Marguerite Porete',
    source: 'The Mirror of Simple Souls',
  },
  {
    quote: 'Yoga is the stilling of the modifications of the mind.',
    author: 'Patanjali',
    source: 'Yoga Sutras',
  },
];

/**
 * Pick today's contemplation based on the day of the year.
 * Same quote for everyone on the same calendar day; rotates daily.
 */
export function todaysContemplation(): Contemplation {
  const now = new Date();
  const start = new Date(now.getFullYear(), 0, 0);
  const diff = now.getTime() - start.getTime();
  const dayOfYear = Math.floor(diff / (1000 * 60 * 60 * 24));
  return contemplations[dayOfYear % contemplations.length];
}
