// llms.txt — a machine-readable index of the library for AI search tools.
// Built from the content collections at build time, so it stays current.
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const BASE = 'https://soulspiritself.com';

export const GET: APIRoute = async () => {
  const [traditions, teachers, texts, themes, essays, signal] = await Promise.all([
    getCollection('traditions'),
    getCollection('teachers'),
    getCollection('texts'),
    getCollection('themes'),
    getCollection('essays'),
    getCollection('signal'),
  ]);

  const lines: string[] = [];
  lines.push('# Soul Spirit Self');
  lines.push('');
  lines.push('> An open library of nondual wisdom across contemplative traditions: foundational texts in public domain translations (readable online, downloadable as PDF/EPUB), teacher profiles, themes that trace single recognitions across traditions, full-text essays, and curated articles.');
  lines.push('');

  lines.push('## Traditions');
  for (const t of traditions.sort((a, b) => a.data.order - b.data.order)) {
    lines.push(`- [${t.data.title}](${BASE}/traditions/${t.slug}/): ${t.data.subtitle}`);
  }
  lines.push('');

  lines.push('## Texts (full text, public domain translations)');
  for (const t of texts.sort((a, b) => a.data.title.localeCompare(b.data.title))) {
    lines.push(`- [${t.data.title}](${BASE}/texts/${t.slug}/): ${t.data.description.split('. ')[0]}.`);
  }
  lines.push('');

  lines.push('## Teachers');
  for (const t of teachers.sort((a, b) => a.data.name.localeCompare(b.data.name))) {
    lines.push(`- [${t.data.name}](${BASE}/teachers/${t.slug}/): ${t.data.summary.split('. ')[0]}.`);
  }
  lines.push('');

  lines.push('## Themes');
  for (const t of themes.sort((a, b) => a.data.order - b.data.order)) {
    lines.push(`- [${t.data.title}](${BASE}/themes/${t.slug}/): ${t.data.subtitle}`);
  }
  lines.push('');

  lines.push('## Essays (full text, public domain)');
  for (const e of essays.sort((a, b) => a.data.order - b.data.order)) {
    lines.push(`- [${e.data.title}](${BASE}/essays/${e.slug}/): ${e.data.author}, ${e.data.year}. ${e.data.description.split('. ')[0]}.`);
  }
  lines.push('');

  lines.push('## The Signal (republished articles)');
  for (const s of signal.sort((a, b) => b.data.date.localeCompare(a.data.date))) {
    lines.push(`- [${s.data.headline}](${BASE}/signal/${s.slug}/): ${s.data.source}. ${s.data.note.split('. ')[0]}.`);
  }
  lines.push('');

  lines.push('## Optional');
  lines.push(`- [Watch](${BASE}/watch/): curated video teachings, filterable by teacher, tradition, and theme`);
  lines.push(`- [Reading](${BASE}/reading/): in-copyright books that supplement the library`);
  lines.push(`- [About](${BASE}/about/): the project and its sourcing standards`);
  lines.push(`- [Signal RSS](${BASE}/signal/rss.xml)`);

  return new Response(lines.join('\n') + '\n', {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
