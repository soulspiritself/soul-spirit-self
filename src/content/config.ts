import { defineCollection, z, reference } from 'astro:content';

const traditions = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    eyebrow: z.string().default('A tradition of nondual wisdom'),
    image: z.string().optional(),
    imagePrompt: z.string().optional(),
    order: z.number().default(99),
    featured: z.boolean().default(false),
    description: z.string(),
    videos: z.array(z.string()).optional(),
    themes: z.array(reference('themes')).optional(),
    leadQuote: z.object({
      text: z.string(),
      attribution: z.string(),
      source: z.string().optional(),
    }).optional(),
  })
});

const teachers = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    // A teacher may belong to one or more traditions. The first entry is treated
    // as the "primary" tradition (used for breadcrumbs, hero eyebrow, etc).
    traditions: z.array(reference('traditions')).min(1),
    born: z.string().optional(),
    died: z.string().optional(),
    summary: z.string(),
    image: z.string().optional(),
    imagePrompt: z.string().optional(),
    related: z.array(reference('teachers')).optional(),
    sourceUrl: z.string().url().optional(),
    videos: z.array(z.string()).optional(),
    themes: z.array(reference('themes')).optional(),
    leadQuote: z.object({
      text: z.string(),
      attribution: z.string(),
      source: z.string().optional(),
    }).optional(),
    // Featured video shown as "Begin here" on the teacher page; falls back to videos[0]
    beginHere: z.string().optional(),
  })
});

const texts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    originalTitle: z.string().optional(),
    subtitle: z.string().optional(),
    tradition: reference('traditions'),
    teacher: reference('teachers').optional(),
    period: z.string().optional(),
    originalLanguage: z.string().optional(),
    composedDate: z.string().optional(),
    translator: z.string().optional(),
    translatorDates: z.string().optional(),
    translationYear: z.string().optional(),
    sourceUrl: z.string().url().optional(),
    sourcePlatform: z.string().optional(),
    licence: z.enum(['public-domain', 'free-distribution', 'cc0', 'cc-by', 'cc-by-nc', 'cc-by-sa', 'cc-by-nc-sa', 'fresh-translation']).default('public-domain'),
    licenceNote: z.string().optional(),
    downloadPdf: z.string().optional(),
    downloadEpub: z.string().optional(),
    downloadTxt: z.string().optional(),
    wordCount: z.number().optional(),
    readingTimeMinutes: z.number().optional(),
    image: z.string().optional(),
    imagePrompt: z.string().optional(),
    description: z.string(),
    related: z.array(reference('texts')).optional(),
    order: z.number().default(99),
    videos: z.array(z.string()).optional(),
    themes: z.array(reference('themes')).optional(),
    leadQuote: z.object({
      text: z.string(),
      attribution: z.string(),
      source: z.string().optional(),
    }).optional(),
  })
});

const themes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    description: z.string(),
    eyebrow: z.string().default('A theme through the library'),
    image: z.string().optional(),
    imagePrompt: z.string().optional(),
    order: z.number().default(99),
    leadQuote: z.object({
      text: z.string(),
      attribution: z.string(),
      source: z.string().optional(),
    }).optional(),
  })
});

const books = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    author: z.string(),
    year: z.string().optional(),
    teacher: reference('teachers').optional(),
    tradition: reference('traditions').optional(),
    blurb: z.string(),
    externalUrl: z.string().optional(),  // accepts external URLs and internal paths
    cover: z.string().optional(),
    publisher: z.string().optional(),
    order: z.number().default(99),
  })
});

export const collections = { traditions, teachers, texts, themes, books };
