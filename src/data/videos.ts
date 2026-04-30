// Curated video library — drawn from the soulspiritself.com YouTube channel.
// Edit this file to add or reorder videos. Many surfaces read from here:
// the homepage Featured grid, the /watch gallery (with filters), and the
// per-page "videos" arrays in tradition / teacher / text frontmatter look up
// titles and captions from the entries below.

export interface Video {
  id: string;            // YouTube video ID
  title: string;
  caption?: string;
  featured?: boolean;
  // Tags used by the /watch filters and the theme pages. All optional.
  teacher?: string;      // teacher slug (e.g. 'robert-adams')
  tradition?: string;    // tradition slug (e.g. 'advaita-vedanta')
  themes?: string[];     // theme slugs (e.g. ['self-inquiry', 'silence'])
}

export const channelUrl = 'https://www.youtube.com/@soulspiritself';

export const videos: Video[] = [
  // ── Bede Griffiths ──
  {
    id: 'hQJ3kcZMHIQ',
    title: 'What You Face at Death Is Unconditional Love',
    caption: 'Bede Griffiths',
    featured: true,
    teacher: 'bede-griffiths',
    tradition: 'christian-mysticism',
    themes: ['death-and-the-deathless', 'love'],
  },

  // ── Nisargadatta Maharaj ──
  {
    id: 'p7H-k6qYRAw',
    title: 'From self to Self',
    caption: 'Nisargadatta Maharaj',
    featured: true,
    teacher: 'nisargadatta-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },
  {
    id: 'Ayniv-MDb0k',
    title: 'Different Pointers, Same Reality',
    caption: 'Nisargadatta & Ramana',
    teacher: 'nisargadatta-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },
  {
    id: 'KUCMhmb1yEw',
    title: 'The I Am and Daily Life',
    caption: 'Nisargadatta Maharaj',
    teacher: 'nisargadatta-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry', 'presence'],
  },
  {
    id: 'IubiX-NBoLk',
    title: 'On the Difficulty of Abiding in I Am',
    caption: 'Nisargadatta Maharaj',
    teacher: 'nisargadatta-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },
  {
    id: 'Fal_fXwGEkc',
    title: 'A Dialogue on Being and the I Am',
    caption: 'Nisargadatta Maharaj',
    teacher: 'nisargadatta-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },
  {
    id: '5I7XGtijfBM',
    title: 'Shakespeare, Ramana, Nisargadatta',
    caption: 'A non-dual contemplation',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },

  // ── Ramana Maharshi ──
  {
    id: '5seQ0ctpOwk',
    title: 'How to Practice Self Inquiry',
    caption: 'Ramana Maharshi',
    featured: true,
    teacher: 'ramana-maharshi',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },

  // ── Robert Adams ──
  {
    id: 'LE3whofS2FM',
    title: 'The First Thing You Must Do Is Love Yourself',
    caption: 'Robert Adams Satsang',
    featured: true,
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['love', 'presence'],
  },
  {
    id: 'RhF18ufcR3A',
    title: 'The Root of All Your Problems Is the I',
    caption: 'Robert Adams',
    featured: true,
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'VHuo15MkU9Y',
    title: 'Because You Exist, Others Exist',
    caption: 'Robert Adams',
    featured: true,
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'vfeB3lDkIeY',
    title: "Don't Try to Stop Your Thoughts. Do This.",
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry', 'silence'],
  },
  {
    id: 'e85QLHYKQk8',
    title: 'What If I Die Before Spiritual Liberation?',
    caption: 'Robert Adams Live Satsang (1992)',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['death-and-the-deathless'],
  },
  {
    id: 'IGlw_y3dkuw',
    title: 'Be Nowhere, and Know Nothing',
    caption: 'Robert Adams Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['silence', 'self-inquiry'],
  },
  {
    id: 'Y8ZvcmY_qdA',
    title: 'Surrender Everything',
    caption: 'Robert Adams Live Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['presence'],
  },
  {
    id: '6deYkoFHsgM',
    title: 'Trust in the Power That Knows the Way',
    caption: 'Robert Adams Live Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['presence'],
  },
  {
    id: 'C2Iu0MQXX3Q',
    title: "Don't Waste Your Life on Fear and Nonsense",
    caption: 'Robert Adams Live Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: '53LBE3ua8yQ',
    title: '"I Am" Is God — The Practice Explained',
    caption: 'Robert Adams Live Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry', 'presence'],
  },
  {
    id: 'wCMYXXu9Hiw',
    title: 'Awakening Is a Joke — There Is Nobody to Wake Up',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'S9vbrIom6L8',
    title: 'The Diamonds Were at His Feet the Whole Time',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['presence'],
  },
  {
    id: 'STsyqsZWgDo',
    title: 'There Is ONLY YOU',
    caption: 'Robert Adams Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'XOFxh0O6Z3A',
    title: "The Mind Is Your Only Problem — and It Doesn't Even Exist",
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'p2ec85Yzlew',
    title: 'On Awakening and the Unreality of the World',
    caption: 'Robert Adams Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'lCu7iWwTXhI',
    title: 'You Have Never Been What You Think You Are',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'PdJL8vZwMMI',
    title: 'The Ego Is a Knot in the Heart — Untie It and Be Free',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry', 'love'],
  },
  {
    id: 'RbfdnlHOm48',
    title: 'Three Keys to Awakening',
    caption: 'Robert Adams Live Satsang',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'mosgWQTOKvM',
    title: 'The 3 Keys to Spiritual Awakening',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'Zw3jmhNq5HQ',
    title: "It's a Simple Technique, and It Works",
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: '_9jE8iU4rbI',
    title: 'The "I Am" Practice — A Quiet Reminder and Reflection',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry', 'silence'],
  },
  {
    id: 'pK-csxB-B5M',
    title: 'True Silence and the Spiritual Heart',
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['silence'],
  },
  {
    id: 'vS7pQZBgQLg',
    title: 'Kill the Ego — Be Happy',
    caption: 'Robert Adams (Sounds Like a Hard Job — But It Isn’t)',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: '2ppJjm64Ek0',
    title: "You've Been Mesmerized into Believing You Are an Image Rather Than a Screen",
    caption: 'Robert Adams',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },
  {
    id: 'YWKyXauAgCs',
    title: 'Awakening Is a Joke — There Is Nobody to Wake Up',
    caption: 'Robert Adams (alternate recording)',
    teacher: 'robert-adams',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },

  // ── John Wheeler ──
  {
    id: 'sTVbOjmwvmw',
    title: 'All Problems Belong to the I',
    caption: 'See through it. John Wheeler.',
    featured: true,
    teacher: 'john-wheeler',
    tradition: 'modern-nonduality',
    themes: ['self-inquiry'],
  },

  // ── Ashtavakra Gita ──
  {
    id: 'ssAcmv3Co9I',
    title: 'The Perfect Spiritual Guide to Enlightenment',
    caption: 'Ashtavakra Gita',
    featured: true,
    tradition: 'advaita-vedanta',
    themes: ['the-witness', 'self-inquiry'],
  },

  // ── Christian Mysticism / cross-tradition ──
  {
    id: 'JZdeMt4GljQ',
    title: 'Where Christianity Meets Advaita',
    caption: 'Mystics, Non-duality, and Oneness',
    featured: true,
    tradition: 'christian-mysticism',
    themes: ['silence', 'love'],
  },

  // ── Gnostic Christianity ──
  {
    id: 'hsUk2CWW0dM',
    title: 'The Secret Book of John',
    caption: 'A reading from the Apocryphon of John',
    featured: true,
    tradition: 'gnostic-christianity',
    themes: ['self-inquiry'],
  },

  // ── Siddharameshwar Maharaj ──
  {
    id: 'FiWVq1T6Tuk',
    title: 'Siddharameshwar Maharaj',
    caption: 'A short reflection on the Sadguru of the Inchagiri Sampradaya',
    featured: true,
    teacher: 'siddharameshwar-maharaj',
    tradition: 'advaita-vedanta',
    themes: ['self-inquiry'],
  },

  // ── Krishnamurti / At the Feet of the Master ──
  {
    id: 'CVZgpSCLKNI',
    title: 'At the Feet of the Master',
    caption: 'Jiddu Krishnamurti — a reading of the 1910 book',
    featured: true,
    teacher: 'jiddu-krishnamurti',
    tradition: 'modern-nonduality',
    themes: ['love', 'presence'],
  },
];

export const featuredVideos = videos.filter(v => v.featured);
