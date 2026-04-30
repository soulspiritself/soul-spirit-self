// Curated video library — drawn from the soulspiritself.com YouTube channel.
// Edit this file to add or reorder videos; both the homepage Featured grid
// and the /watch gallery read from here.

export interface Video {
  id: string;            // YouTube video ID
  title: string;
  caption?: string;
  featured?: boolean;
}

export const channelUrl = 'https://www.youtube.com/@soulspiritself';

export const videos: Video[] = [
  {
    id: 'p7H-k6qYRAw',
    title: 'From self to Self',
    caption: 'Nisargadatta Maharaj',
    featured: true,
  },
  {
    id: 'hQJ3kcZMHIQ',
    title: 'What You Face at Death Is Unconditional Love',
    caption: 'Bede Griffiths',
    featured: true,
  },
  {
    id: 'LE3whofS2FM',
    title: 'The First Thing You Must Do Is Love Yourself',
    caption: 'Robert Adams Satsang',
    featured: true,
  },
  {
    id: 'RhF18ufcR3A',
    title: 'The Root of All Your Problems is the I',
    caption: 'Robert Adams',
    featured: true,
  },
  {
    id: 'VHuo15MkU9Y',
    title: 'Because You Exist, Others Exist',
    caption: 'End the Dream',
    featured: true,
  },
  {
    id: 'ssAcmv3Co9I',
    title: 'The Perfect Spiritual Guide to Enlightenment',
    caption: 'Ashtavakra Gita',
    featured: true,
  },
  {
    id: '5seQ0ctpOwk',
    title: 'How to practice Self Inquiry',
    caption: 'Ramana Maharshi',
    featured: true,
  },
  {
    id: 'JZdeMt4GljQ',
    title: 'Where Christianity Meets Advaita',
    caption: 'Mystics, Non-duality, and Oneness',
    featured: true,
  },
  {
    id: 'sTVbOjmwvmw',
    title: 'All problems belong to the I',
    caption: 'See through it. John Wheeler',
    featured: true,
  },
  {
    id: 'hsUk2CWW0dM',
    title: 'The Secret Book of John',
    caption: 'A reading from the Apocryphon of John',
    featured: true,
  },
  {
    id: 'FiWVq1T6Tuk',
    title: 'Siddharameshwar Maharaj',
    caption: 'A short reflection on the Sadguru of the Inchagiri Sampradaya',
    featured: true,
  },
  {
    id: 'CVZgpSCLKNI',
    title: 'At the Feet of the Master',
    caption: 'Jiddu Krishnamurti — a reading of the 1910 book',
    featured: true,
  },
];

export const featuredVideos = videos.filter(v => v.featured);
