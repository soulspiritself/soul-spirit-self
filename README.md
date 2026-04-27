# Soul Spirit Self

Contemplative content hub. Astro-built, Netlify-deployed, edited via Markdown.

## Quick start

```bash
npm install
npm run dev
```

The dev server runs at `http://localhost:4321`. Edit any file in `src/` and the browser reloads.

```bash
npm run build
```

Builds the static site into `dist/`. This is what Netlify runs on every git push.

```bash
npm run preview
```

Serves the production build locally to verify before deploying.

## How content works

All content lives in `src/content/` as Markdown files with YAML frontmatter. Three collections:

- `traditions/` — one file per tradition (Advaita Vedanta, Christian Mysticism, etc.)
- `teachers/` — one file per teacher
- `texts/` — one file per source text

The schemas in `src/content/config.ts` define what frontmatter each collection needs. If a file is missing a required field, the build fails with a clear error.

## How to add a new text

1. Create a new file like `src/content/texts/avadhuta-gita.md`
2. Copy the frontmatter pattern from an existing text file
3. Write the description and the text body in Markdown
4. Save. The text appears automatically on its tradition page and gets its own URL at `/texts/avadhuta-gita/`

## How to add a new tradition

1. Create `src/content/traditions/<slug>.md` with the right frontmatter
2. Add teachers and texts that reference this tradition (set `tradition: <slug>` in their frontmatter)
3. The tradition automatically appears on the home page and traditions index

## How to change the design

- **Colours**: edit CSS variables in `src/styles/global.css`
- **Typography**: edit the same file
- **Page layouts**: edit files in `src/pages/`
- **Components**: edit files in `src/components/`

A change to one template updates every page that uses it.

## Deployment

Connected to Netlify. Push to the main git branch and the site rebuilds and deploys in 30-60 seconds.

DNS is via IONOS (already set up).

## File structure

```
src/
├── content/          # All editable content as Markdown
│   ├── config.ts     # Schemas for each collection
│   ├── traditions/
│   ├── teachers/
│   └── texts/
├── layouts/          # Page wrappers
├── components/       # Reusable UI pieces
├── pages/            # URL routing
└── styles/global.css # Colour palette and typography
```

## Visual identity

Cosmic dark palette: deep navy base, warm gold accent, off-white text. Cormorant Garamond for serif (headings, body of texts), Inter for sans (UI). Edit the variables in `global.css` to retheme everything.

## Image strategy

All imagery comes from Imagen 4. Each piece of content has an `imagePrompt` field describing the image that should be generated. Generated images go in `public/images/` and are referenced by the `image` field in the content frontmatter.

Image placeholders show "Imagen 4 placeholder" until the real image is generated and added.

## Attribution

Every text page renders the AttributionBlock component, which reads from the text's frontmatter (translator, dates, source URL, licence). One source of truth, consistent display everywhere.
