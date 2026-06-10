// RSS feed for The Signal.
// Includes both hosted (republished, full content via on-site URL) and external
// (linkout-only) stories. Newest-first. Discoverable via <link rel="alternate">
// in BaseLayout when on a /signal/* page.
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { signalStories, categoryLabel } from '../../data/signal';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const hosted = (await getCollection('signal')).map(s => ({
    title: s.data.headline,
    description: s.data.note,
    pubDate: new Date(s.data.date + 'T10:00:00Z'),
    link: `/signal/${s.slug}/`,                       // resolved against context.site
    categories: [categoryLabel[s.data.category], 'The Signal'],
    customData: [
      `<source url="${s.data.sourceUrl}">${s.data.source}</source>`,
      s.data.author ? `<dc:creator><![CDATA[${s.data.author}]]></dc:creator>` : '',
    ].filter(Boolean).join(''),
  }));

  const hostedSourceUrls = new Set((await getCollection('signal')).map(s => s.data.sourceUrl));
  const external = signalStories
    .filter(s => !hostedSourceUrls.has(s.url))
    .map(s => ({
      title: s.headline,
      description: s.note,
      pubDate: new Date(s.date + 'T10:00:00Z'),
      link: s.url,
      categories: [categoryLabel[s.category], 'The Signal'],
      customData: `<source>${s.source}</source>`,
    }));

  const items = [...hosted, ...external].sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime());

  return rss({
    title: 'The Signal — Soul Spirit Self',
    description: 'Stories from consciousness research, contemplative practice, and the wisdom traditions, curated as they surface.',
    site: context.site!,
    items,
    customData: '<language>en-gb</language>',
    xmlns: { dc: 'http://purl.org/dc/elements/1.1/' },
  });
}
