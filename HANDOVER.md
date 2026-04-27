# Soul Spirit Self — Handover

Everything you need to take this forward, whether you continue working with me through Cowork or hand the project to a developer.

## What this project is

A static-site reboot of soulspiritself.com built in Astro, designed as a contemplative content hub and as a portfolio piece for institutional pitches. Currently structurally complete for one tradition (Advaita Vedanta) with 9 texts and 7 teachers, ready to scale to the remaining six traditions.

## What's in this folder

```
soul-spirit-self/
├── HANDOVER.md            ← you are here
├── README.md              ← day-to-day workflow reference
├── package.json           ← Astro + dependencies
├── astro.config.mjs
├── netlify.toml           ← Netlify deploy config (already correct)
├── tsconfig.json
├── .gitignore
├── .env.example           ← Imagen API key template
├── public/
│   ├── favicon.svg
│   └── images/            ← Imagen 4 outputs go here
├── scripts/
│   └── generate-images.py ← Imagen automation
└── src/
    ├── content/           ← All editable content as Markdown
    │   ├── config.ts      ← Schemas for each collection
    │   ├── traditions/    ← 1 file per tradition (currently: Advaita)
    │   ├── teachers/      ← 1 file per teacher (currently: 7)
    │   └── texts/         ← 1 file per source text (currently: 9)
    ├── layouts/
    ├── components/
    ├── pages/
    └── styles/global.css  ← Colour palette, typography (single source of truth)
```

## Recommended path: continue via Cowork

You're a content person, not a developer. The original idea was that I keep iterating on the site as you describe changes. That's still the right setup. Here's how to make it work for real, persistently:

### One-time setup (10 minutes)

1. **Move this entire folder to `~/Documents/SoulSpiritSelf/`** on your Mac. (Or wherever you want, but `~/Documents/SoulSpiritSelf/` is what the rest of this guide assumes.)

2. **Make sure your Imagen API key is in `~/Documents/Claude/.env`** as your existing setup specifies. If it's already there from prior work, no action needed.

3. **Start a fresh Cowork session and select `~/Documents/SoulSpiritSelf/` as the working folder** when Cowork prompts you. From that point on every change I make happens directly in your real folder.

4. **Tell me you've done it.** First thing I'll do is run the install (`npm install`) and the first build to verify everything still works on your Mac. Then I'll run the Imagen workflow to generate the 17 Advaita images directly into `public/images/`.

### Ongoing workflow

You describe a change. I make it. Examples:

- "Generate the Christian Mysticism section, full lineage like Advaita."
- "The hero font feels too heavy. Try something lighter."
- "Add a Buddhism page using the same approach."
- "Fix the typo in the Ashtavakra intro."
- "Make a blog post about Ramana's teaching on self-enquiry."
- "I want the texts to have a Sanskrit toggle."

Each change becomes a few file edits, a verification build, and (when ready) a git push that triggers Netlify to redeploy. You don't touch any of that machinery.

## Alternative path: hand it to a developer or use it yourself in code

If you'd rather work on the code directly or hand it to someone who codes, the project is a standard Astro project. Anyone familiar with Astro can pick it up immediately.

### First-run commands

```bash
cd ~/Documents/SoulSpiritSelf
npm install
npm run dev
```

The dev server runs at `http://localhost:4321` with hot reload. Edit any `.md` or `.astro` file and the browser updates.

```bash
npm run build      # produces /dist for deployment
npm run preview    # serves the built site locally to verify
```

### Adding content

Every piece of content is one Markdown file with YAML frontmatter at the top. The schemas in `src/content/config.ts` enforce the required fields. To add a new text:

1. Create `src/content/texts/my-new-text.md`
2. Copy frontmatter pattern from an existing file
3. Write the text body
4. Save. The text auto-appears on its tradition page and gets a URL at `/texts/my-new-text/`

To add a new tradition or teacher, same pattern in the corresponding subfolder.

### Changing the design

- All colours and typography live in CSS variables at the top of `src/styles/global.css`. Edit there to retheme the entire site.
- Page layouts are in `src/layouts/` and `src/pages/`.
- Reusable components in `src/components/`.

## Deploy to soulspiritself.com (when ready)

Your existing Netlify + IONOS setup carries over unchanged. Steps:

### One-time

1. **Create a GitHub repository** (private or public, your call). Name it `soul-spirit-self`.
2. **Push the local folder to GitHub:**

   ```bash
   cd ~/Documents/SoulSpiritSelf
   git init
   git add .
   git commit -m "Initial Astro build"
   git remote add origin https://github.com/your-username/soul-spirit-self.git
   git branch -M main
   git push -u origin main
   ```

3. **Connect the repo in Netlify:**
   - Open Netlify dashboard
   - Add new site → import from Git → select your repo
   - Build command: `npm run build`
   - Publish directory: `dist`
   - Click Deploy

4. **Point soulspiritself.com at the new site:**
   - In Netlify dashboard for this site → Domain settings
   - Add custom domain → `soulspiritself.com`
   - Netlify gives you DNS instructions; if you previously set up the domain via IONOS pointing at Netlify, no further action needed. Otherwise update your IONOS DNS records as Netlify shows.

5. **Switch the live domain.** Netlify will swap soulspiritself.com from the old landing page to the new build automatically once DNS confirms.

### Going forward

Every `git push` triggers Netlify to rebuild and redeploy, usually in 30-60 seconds. If you continue via Cowork, I run the git push for you each time you approve a change. If you go the code route, you push manually.

## Imagen 4 workflow (Stage 2 imagery)

The site currently uses dark placeholder boxes labelled "Imagen 4 placeholder" until real imagery is generated. The complete shot list with prompts is in `Imagen-4-Prompts-Brief.docx` in the parent folder.

### Automated (Cowork path)

Once I have filesystem access, I read your API key from `~/Documents/Claude/.env`, run all 17 prompts in sequence, save the outputs to `public/images/` with the correct filenames, and rebuild the site. You watch it populate live. Cost: roughly $0.70 for the full Stage 2 batch.

### Manual (code path)

1. Copy `.env.example` to `.env` and add your Google API key
2. Run `python scripts/generate-images.py` (script included in this folder)
3. Images save to `public/images/` automatically with the correct filenames
4. Rebuild and verify

You can also run prompts one at a time through your existing Imagen setup; the brief shows the filename each output should use.

## Current state honest assessment

### Done
- Site architecture, page templates, dynamic routing
- Full visual identity (cosmic dark + warm gold + Cormorant Garamond)
- Universal attribution component
- SEO foundations (meta tags, Open Graph, sitemap, schema markup on text pages)
- Advaita Vedanta tradition fully populated: 9 texts, 7 teachers, full lineage from Gaudapada through Shankara to the modern Inchagiri masters
- All Advaita content sourced from confirmed PD or freely-distributable material with proper licence notes
- Netlify deploy config ready
- Build verified: 12 routes generating cleanly

### Not yet done
- Imagen images (placeholders in place, prompts ready in brief)
- Christian Mysticism, Buddhist Nonduality, Sufism, Taoism, Modern Nonduality, Kashmir Shaivism (skeleton ready, content not populated)
- Blog/journal section (template exists in nav, no content yet)
- Email signup integration (Kit/ConvertKit)
- Retreat directory
- Resources section
- Search
- Connection to live soulspiritself.com domain

### Strategic decisions still open
- Whether to translate the unhostable texts (Inchagiri, Kashmir Shaivism, Rhineland women mystics) ourselves to unlock those gaps
- Whether Modern Nonduality becomes a directory of biographical pages with outbound links, or gets dropped entirely
- Whether to add a Sanskrit/original-language toggle on text pages
- Whether to add ElevenLabs audio narration for texts

## Documents in the parent folder

These are reference materials I produced during planning and research. Live alongside this project folder.

- **Phase-Zero-Soul-Spirit-Self-Plan.docx** — the full project plan, site architecture, build sequence, content workflow
- **Public-Domain-Sources-Catalog.docx** — first-pass catalog of PD sources for the original teacher list
- **Public-Domain-Lineage-Catalog.docx** — expanded catalog going down each tradition's lineage (~100 sources)
- **Imagen-4-Prompts-Brief.docx** — complete shot list with prompts for Stage 2

## What to ask me to do next

If you continue via Cowork, here are the natural next moves in order of momentum:

1. **Grant filesystem access** (one click), I move the project to your Mac and run the Imagen batch
2. **Bulk-populate Christian Mysticism** the same way Advaita was populated (next biggest tradition by PD coverage)
3. **Set up GitHub + Netlify** so the site goes live (5-10 min interactive task)
4. **Write the first 3 blog posts** to give the journal section content
5. **Generate the Christian Mysticism imagery batch** via Imagen
6. **Then continue tradition by tradition until full Stage 4 completion**

If you go the code route, the README.md is your day-to-day reference. The HANDOVER.md (this file) is the strategic context. The four .docx files in the parent folder are the deeper planning material.

## Questions, decisions, blockers

Any time during the build, if you want me to pause and decide something, just say. The project is set up so individual decisions (font choice, attribution wording, which translator to use for a given text) can be made in isolation without breaking anything else.
