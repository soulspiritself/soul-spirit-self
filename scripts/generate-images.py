#!/usr/bin/env python3
"""
Soul Spirit Self - Imagen 4 image generation
Generates all images defined in IMAGES list using Google's Imagen 4 API.

Setup:
  pip install google-genai python-dotenv pillow
  Ensure GOOGLE_API_KEY is set in ~/Documents/Claude/.env or in ./.env

Usage:
  python scripts/generate-images.py             # generates all missing images
  python scripts/generate-images.py --force     # regenerate everything
  python scripts/generate-images.py --only ramana-maharshi   # one image
"""

import os
import sys
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types
except ImportError:
    print("Missing dependencies. Run: pip install google-genai python-dotenv")
    sys.exit(1)

# ── Locate .env ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_LOCATIONS = [
    PROJECT_ROOT / ".env",
    Path.home() / "Documents" / "Claude" / ".env",
]
for env_path in ENV_LOCATIONS:
    if env_path.exists():
        load_dotenv(env_path)
        print(f"Loaded env from {env_path}")
        break
else:
    print("No .env found. Looked in:", ", ".join(str(p) for p in ENV_LOCATIONS))
    sys.exit(1)

API_KEY = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("GOOGLE_API_KEY not set in .env")
    sys.exit(1)

OUTPUT_DIR = PROJECT_ROOT / "public" / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Image definitions ──
STYLE_PREFIX = (
    "Photorealistic painterly hybrid style, contemplative atmosphere, "
    "deep cosmic blue and warm amber palette, soft golden lighting, "
    "rich shadows, no text, no watermarks, no people unless specified, "
)

IMAGES = [
    # ── Tradition heroes ──
    {
        "filename": "tradition-advaita-vedanta.jpg",
        "aspect": "16:9",
        "prompt": STYLE_PREFIX + (
            "Arunachala mountain in southern India at golden hour, viewed from a slight distance "
            "across an open plain, the sacred hill silhouetted against a vast deep blue twilight "
            "sky scattered with faint stars, a single warm point of light glowing near the summit "
            "suggesting the inner fire of the mountain, low golden mist on the plain, no people, "
            "no buildings, no text, evocative and serene, wide cinematic composition"
        ),
    },
    # ── Text images ──
    {
        "filename": "text-mandukya-upanishad.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single luminous concentric ring of warm gold suspended in deep cosmic blue space, "
            "with three faint outer rings receding into shadow representing waking, dream, and "
            "deep sleep, and a single radiant point of pure gold at the centre representing "
            "turiya the fourth, minimalist sacred geometry composition, contemplative atmosphere, "
            "no text, no watermarks"
        ),
    },
    {
        "filename": "text-isha-upanishad.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A vast warm golden radiance enveloping a small dark spherical world held suspended "
            "at its centre, the radiance soft and limitless extending outward to the edge of the "
            "frame, the small world held tenderly within it, faint stars in the surrounding "
            "cosmic blue beyond, contemplative atmosphere, painterly minimalist composition, "
            "no text, no watermarks"
        ),
    },
    {
        "filename": "text-katha-upanishad.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An empty ancient Indian stone chariot drawn by five luminous horses on an open plain "
            "at dusk, the chariot itself silent and unoccupied, the reins still and untouched, "
            "deep cosmic blue sky above with faint stars, soft amber dawn light breaking on the "
            "distant horizon, painterly contemplative composition, no driver, no people, no text, "
            "no watermarks"
        ),
    },
    {
        "filename": "text-mundaka-upanishad.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Two birds perched on the slender branch of a single dark tree silhouetted against a "
            "vast cosmic blue night sky scattered with faint stars, one bird leaning forward to "
            "take a small fruit hanging on the branch, the other still and watching with quiet "
            "attention, soft warm golden light from a single point on the horizon, painterly "
            "contemplative composition, no text, no watermarks"
        ),
    },
    {
        "filename": "text-brahma-sutras.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single fine golden thread descending vertically through a vast deep cosmic blue "
            "space, passing through a series of nested concentric translucent circles each glowing "
            "softly from within, the thread continuous and unbroken from top to bottom of the "
            "frame, contemplative sacred geometry composition, painterly minimalist style, "
            "no text, no watermarks"
        ),
    },
    {
        "filename": "text-mandukya-karika.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic representation of the four states of consciousness, four concentric circular "
            "rings, the outermost a faint silver representing waking, the next a deeper translucent "
            "blue representing dream, the next a darker indigo representing deep sleep, the innermost "
            "a single radiant gold point representing turiya, set against an infinite dark cosmic "
            "background with subtle stars, contemplative composition, no text"
        ),
    },
    {
        "filename": "text-yoga-vasistha.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An ancient Indian sage Vasistha with long silver beard wearing a simple ochre dhoti, "
            "sitting cross-legged beneath a vast spreading banyan tree in ancient India, instructing "
            "a young Indian prince Rama in simple traditional Indian attire who sits in dawn light "
            "at his feet, view from a respectful distance, the figures small against the immense "
            "tree and sky, deep golden dawn rising behind them, painterly contemplative composition "
            "in the spirit of traditional South Asian temple painting, no text, no watermarks, no "
            "European or biblical figures, no signature"
        ),
    },
    {
        "filename": "text-ashtavakra-gita.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single ripple of golden light spreading across the surface of dark still water, "
            "viewed from above, the source of the ripple a single point of warm radiance at the "
            "centre, the surrounding water deep cosmic blue with the faint reflection of stars, "
            "minimalist contemplative composition, no text"
        ),
    },
    {
        "filename": "text-avadhuta-gita.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A solitary figure of a wandering sage walking at the edge of a forest at twilight, "
            "only the silhouette visible, the forest deep blue and the open sky beyond it streaked "
            "with faint amber and stars, sense of complete freedom and renunciation, contemplative "
            "painterly composition, no text"
        ),
    },
    {
        "filename": "text-tripura-rahasya.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A glowing yantra of three nested triangles in deep gold lines, the outermost largest "
            "and the innermost smallest, all centred on a single point, set against an infinite "
            "dark cosmic blue background with subtle radiating soft golden light, sacred geometry "
            "composition, contemplative atmosphere, no text"
        ),
    },
    {
        "filename": "text-vivekachudamani.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single many-faceted crystalline jewel suspended in deep cosmic space, refracting "
            "golden light into rays that extend into the surrounding darkness, the jewel itself "
            "translucent with inner light, contemplative painterly composition, no text"
        ),
    },
    {
        "filename": "text-atma-bodha.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single radiant point of warm golden light at the centre of an infinite dark expanse, "
            "with subtle rays extending outward dispelling the surrounding darkness, like a sunrise "
            "seen from far in space, minimalist contemplative composition, no text"
        ),
    },
    {
        "filename": "text-aparokshanubhuti.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An open eye opening at the centre of a mandala of concentric golden rings against a "
            "deep cosmic blue background, the eye itself radiant with inner light, the rings "
            "extending outward in soft graduated luminosity, contemplative sacred geometry, no text"
        ),
    },
    {
        "filename": "text-yoga-sutras.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single steady flame burning in a small clay oil lamp set on a dark stone surface, "
            "the flame perfectly still and warm gold, the surrounding darkness vast with faint "
            "stars suggesting the night sky beyond, intimate yet vast composition, contemplative "
            "atmosphere, no text"
        ),
    },
    # ── Teacher portraits ──
    {
        "filename": "teacher-gaudapada.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of an ancient Indian sage Gaudapada, seated cross-legged "
            "in deep meditation, eyes half-closed, long silver beard, simple ochre robe, soft warm "
            "dawn light from above, banyan tree leaves visible behind him, painterly traditional "
            "South Asian style with contemplative warmth, square composition centred on the figure, "
            "no text"
        ),
    },
    {
        "filename": "teacher-shankara.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic portrait of Adi Shankara, a young Indian monk in his late twenties, shaved "
            "head, intense direct gaze, wearing simple saffron robes, holding a manuscript in one "
            "hand, soft golden light from one side, painterly traditional South Asian style with "
            "contemplative gravitas, square composition centred on the figure, no text"
        ),
    },
    {
        "filename": "teacher-ramana-maharshi.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic portrait of Sri Ramana Maharshi as an elderly Indian sage in his late "
            "sixties, shaved head, gentle silvery white beard, deep peaceful eyes with a slight "
            "downward gaze, wearing only a simple white loincloth, seated on a stone bench, soft "
            "warm afternoon light filtered through trees, contemplative atmosphere reminiscent of "
            "mid-twentieth century photographs from Tiruvannamalai, square composition centred on "
            "his face and shoulders, no text"
        ),
    },
    {
        "filename": "teacher-nisargadatta-maharaj.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic head and shoulders portrait of an elderly Indian man in his late "
            "seventies with a full head of grey-white hair brushed back, weathered intense face "
            "with deep peaceful direct gaze, sparse white moustache, wearing a simple white kurta "
            "shirt, soft warm afternoon light from above and to one side, dim interior background "
            "of a simple Indian room, contemplative atmosphere in the visual style of mid-twentieth "
            "century black-and-white documentary photography but with warm tone, square composition "
            "centred tightly on his face and shoulders, no text, no watermarks, no signature, no "
            "decorative borders, no flowers, no logos"
        ),
    },
    {
        "filename": "teacher-atmananda-krishna-menon.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic portrait of Sri Atmananda Krishna Menon as a dignified middle-aged "
            "Kerala Indian man, dark hair brushed back, neat moustache, serious contemplative "
            "direct gaze, wearing a simple white shirt with a dark waistcoat, soft warm photographic "
            "lighting reminiscent of mid-twentieth century studio portraits, square composition "
            "centred on his face and shoulders, no text"
        ),
    },
    {
        "filename": "teacher-siddharameshwar-maharaj.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic portrait of Sri Siddharameshwar Maharaj as an Indian sage in his "
            "forties, shaved head, warm direct gaze, simple white robe, soft afternoon photographic "
            "light reminiscent of early-twentieth century portraits from Maharashtra, contemplative "
            "warmth, square composition centred on his face and shoulders, no text"
        ),
    },
    {
        "filename": "teacher-ranjit-maharaj.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic portrait of Sri Ranjit Maharaj as a very elderly Indian sage in his "
            "eighties, full head of white hair, warm gentle smile creasing his eyes, wearing a "
            "simple white shirt, soft warm afternoon light from above and to one side, contemplative "
            "warmth reminiscent of late-1990s photographs from Mumbai, square composition centred "
            "on his face and shoulders, no text"
        ),
    },
    # ────────────────────────────────────────────────────────────────────
    # CHRISTIAN MYSTICISM
    # ────────────────────────────────────────────────────────────────────
    {
        "filename": "tradition-christian-mysticism.jpg",
        "aspect": "16:9",
        "prompt": STYLE_PREFIX + (
            "A vast Romanesque cathedral nave at dawn, deep stone arches receding into shadow, "
            "a single shaft of warm golden light falling diagonally through a high lancet window "
            "onto the empty stone floor, the rest of the interior in deep cosmic blue twilight "
            "shadow, no people, no text, contemplative atmosphere, wide cinematic composition, "
            "evocative and serene"
        ),
    },
    # ── Christian texts ──
    {
        "filename": "text-confessions.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An open ancient leather-bound codex resting on a dark stone surface, thick parchment "
            "pages catching a single beam of warm golden light from above, the rest of the room "
            "fading into deep cosmic blue shadow, intimate scholarly contemplative atmosphere, "
            "no text legible on the pages, no watermarks, painterly chiaroscuro composition"
        ),
    },
    {
        "filename": "text-sermons-on-song-of-songs.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single deep amber rose blooming against a vast deep cosmic blue night sky scattered "
            "with faint stars, soft golden light gently illuminating the petals from one side, "
            "minimalist contemplative composition, painterly atmospheric style, no text, no "
            "watermarks"
        ),
    },
    {
        "filename": "text-eckhart-sermons.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An empty vault of dark cosmic blue space with a single point of warm golden light "
            "at its absolute centre, the light pure and silent, faint subtle stars in the "
            "surrounding void, no walls or boundaries visible, contemplative apophatic atmosphere, "
            "minimalist composition, no text, no watermarks"
        ),
    },
    {
        "filename": "text-theologia-germanica.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "An open hand seen from the side, gently letting go of a small warm golden flame "
            "which floats upward into a vast dark cosmic blue sky scattered with subtle stars, "
            "the hand simple and ordinary, the gesture of release, contemplative composition, "
            "painterly style, no text, no watermarks"
        ),
    },
    {
        "filename": "text-tauler-sermons.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A small candle flame burning steadily on a simple wooden table inside a medieval "
            "Gothic chapel, a single shaft of warm golden light from a high stone window meeting "
            "the candle, deep cosmic blue interior shadow, no people, contemplative intimate "
            "atmosphere, painterly style, no text, no watermarks"
        ),
    },
    {
        "filename": "text-revelations-of-divine-love.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A small hazelnut resting in an open palm, glowing faintly with warm golden inner "
            "light, the hand and forearm seen from above against a deep cosmic blue background "
            "scattered with subtle stars, contemplative tender atmosphere, painterly style, no "
            "text, no watermarks"
        ),
    },
    {
        "filename": "text-cloud-of-unknowing.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single dark cloud illuminated softly from within by warm golden light, suspended "
            "in a vast dark cosmic blue sky scattered with subtle stars, the cloud both opaque "
            "and luminous, mysterious apophatic atmosphere, painterly atmospheric composition, "
            "no text, no watermarks"
        ),
    },
    {
        "filename": "text-dark-night-of-the-soul.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single small dark figure walking down a stone staircase that descends into a "
            "vast deep cosmic blue void scattered with faint stars, distant warm amber light "
            "barely visible far below, the descent peaceful and intentional rather than fearful, "
            "contemplative atmosphere, painterly dramatic composition, no text, no watermarks"
        ),
    },
    {
        "filename": "text-interior-castle.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A faceted crystal castle suspended in a vast cosmic blue space, faint warm golden "
            "light glowing from its innermost central chamber outward through the translucent "
            "concentric walls, sacred geometry composition, contemplative atmosphere, painterly "
            "style, no text, no watermarks"
        ),
    },
    {
        "filename": "text-practice-of-the-presence.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "A single open hand from below cradling a small steady warm golden flame, the hand "
            "weathered and ordinary, the rest of the composition deep cosmic blue with faint "
            "stars, intimate humble contemplative atmosphere, painterly style, no text, no "
            "watermarks"
        ),
    },
    # ── Christian teacher portraits ──
    {
        "filename": "teacher-augustine-of-hippo.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Augustine of Hippo as a North African bishop in the "
            "early fifth century, dark olive skin, dark hair greying at the temples, neatly "
            "trimmed dark beard, intelligent contemplative gaze with eyes raised slightly upward, "
            "wearing a simple Roman tunic and an ecclesiastical mantle, soft warm golden light, "
            "painterly classical Mediterranean style, square composition centred on his face and "
            "shoulders, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-bernard-of-clairvaux.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Bernard of Clairvaux as a twelfth-century Cistercian "
            "abbot in his fifties, lean ascetic European features, white woollen monastic habit "
            "with the cowl raised, contemplative serious downward gaze, soft warm light from one "
            "side suggesting a simple monastic interior, painterly medieval style, square "
            "composition centred on his face and shoulders, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-meister-eckhart.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Meister Eckhart as a thirteenth-century German "
            "Dominican friar in his sixties, lean intelligent European features, short tonsured "
            "grey hair, black and white Dominican habit, deep contemplative direct gaze, soft "
            "golden light from one side, painterly Gothic style, square composition centred on "
            "his face and shoulders, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-johannes-tauler.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Johannes Tauler as a fourteenth-century German "
            "Dominican friar in his fifties, weathered kindly European features, short grey hair, "
            "black and white Dominican habit, soft contemplative compassionate expression, warm "
            "golden light from one side suggesting a simple Gothic interior, painterly medieval "
            "style, square composition centred on his face and shoulders, no text, no watermarks, "
            "no signature"
        ),
    },
    {
        "filename": "teacher-julian-of-norwich.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Julian of Norwich as a fourteenth-century English "
            "anchoress in her fifties, kind weathered European features, simple grey woollen "
            "habit and white wimple, contemplative gentle gaze, soft warm light streaming through "
            "a small stone window onto her face, painterly medieval English style, square "
            "composition centred on her face and shoulders, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-john-of-the-cross.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of John of the Cross as a sixteenth-century Spanish "
            "Carmelite friar in his forties, lean ascetic Spanish features, dark hair and short "
            "dark beard, deep peaceful contemplative direct gaze, wearing a simple brown Carmelite "
            "habit, soft warm Spanish light from one side, painterly Spanish Golden Age style, "
            "square composition centred on his face and shoulders, no text, no watermarks, no "
            "signature"
        ),
    },
    {
        "filename": "teacher-teresa-of-avila.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Teresa of Avila as a sixteenth-century Spanish "
            "Carmelite nun in her late fifties, intelligent kindly Spanish features, weathered "
            "warm face, brown Carmelite habit and black veil, contemplative direct gaze with a "
            "trace of warmth, soft warm light from one side, painterly Spanish Golden Age style, "
            "square composition centred on her face and shoulders, no text, no watermarks, no "
            "signature"
        ),
    },
    {
        "filename": "teacher-brother-lawrence.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Brother Lawrence as a seventeenth-century French "
            "Carmelite lay brother in his sixties, weathered kindly French peasant face with a "
            "gentle smile, short grey hair, simple brown lay brother's habit, hands folded humbly, "
            "soft warm candlelight from below suggesting a humble kitchen interior, painterly "
            "Baroque style, square composition centred on his face and shoulders, no text, no "
            "watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-hildegard-of-bingen.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of an elderly twelfth-century European Benedictine "
            "Christian abbess, seventy-year-old white woman with intelligent serene wrinkled "
            "face, traditional medieval Benedictine black monastic habit and long white linen "
            "veil framing her face, holding a small leather-bound illuminated manuscript in her "
            "hands, soft warm golden light streaming through a small Romanesque stone window, "
            "painterly medieval style evoking Romanesque manuscript illumination, square "
            "composition tightly centred on her face and shoulders, contemplative atmosphere, "
            "no animals, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-mechthild-of-magdeburg.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of Mechthild of Magdeburg as a thirteenth-century German "
            "Beguine in her fifties, gentle contemplative European features, simple grey woollen "
            "robe and white linen veil, soft direct gaze, soft warm Northern European light, "
            "painterly medieval Northern European style, square composition centred on her face "
            "and shoulders, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-hadewijch.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of a young thirteenth-century Flemish medieval European "
            "religious woman, a Beguine lay sister in her thirties, white European complexion, "
            "intelligent contemplative serene face, dressed in a simple plain light grey woollen "
            "religious robe and a long white linen veil covering her hair, holding a small "
            "handwritten parchment manuscript, soft warm Northern European afternoon light from "
            "a small Gothic window, painterly medieval Flemish religious style, square "
            "composition tightly centred on her face and shoulders, no modern clothing, no "
            "sunglasses, no beach, no text, no watermarks, no signature"
        ),
    },
    {
        "filename": "teacher-marguerite-porete.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Symbolic painterly portrait of a thirteenth-century French medieval European "
            "religious woman, a Beguine lay sister in her fifties, white European complexion, "
            "intelligent serious deeply weathered face, contemplative direct unwavering gaze, "
            "dressed in a simple plain grey woollen religious robe and a long white linen veil "
            "covering her hair, soft warm afternoon light from a small Gothic stone window, "
            "painterly French medieval religious style, square composition tightly centred on "
            "her face and shoulders, no food, no cake, no modern objects, no text, no watermarks, "
            "no signature"
        ),
    },
    {
        "filename": "teacher-bede-griffiths.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic head and shoulders portrait of an elderly white European Christian "
            "monk in his eighties, long flowing white hair brushed back and full white beard, "
            "gentle deep peaceful gaze, fair complexion weathered by decades in tropical climate, "
            "wearing a simple saffron robe of an Indian Christian ashram dweller draped over one "
            "shoulder, soft warm afternoon light, contemplative atmosphere reminiscent of "
            "late-twentieth-century documentary photography from southern India, square "
            "composition tightly centred on his face and shoulders, no text, no watermarks, no "
            "signature"
        ),
    },
    {
        "filename": "teacher-anthony-de-mello.jpg",
        "aspect": "1:1",
        "prompt": STYLE_PREFIX + (
            "Photorealistic head and shoulders portrait of Anthony de Mello as an Indian Jesuit "
            "priest in his fifties, dark hair flecked with grey neatly combed, warm intelligent "
            "Goan-Indian face with a gentle subtle smile creasing his eyes, wearing a simple "
            "black clerical shirt with a Roman collar, soft warm afternoon light from one side, "
            "contemplative atmosphere reminiscent of mid-1980s photographs from his Lonavla "
            "retreat centre in Maharashtra, square composition tightly centred on his face and "
            "shoulders, no text, no watermarks, no signature"
        ),
    },
]

# ── Generate ──
def generate_one(client, image_def, force=False):
    output_path = OUTPUT_DIR / image_def["filename"]
    if output_path.exists() and not force:
        print(f"  [skip] {image_def['filename']} (already exists)")
        return False

    print(f"  [gen]  {image_def['filename']} ({image_def['aspect']})")
    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=image_def["prompt"],
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=image_def["aspect"],
                output_mime_type="image/jpeg",
            ),
        )
        image = response.generated_images[0].image
        with open(output_path, "wb") as f:
            f.write(image.image_bytes)
        print(f"         saved to {output_path.name}")
        return True
    except Exception as e:
        print(f"         FAILED: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="regenerate existing images")
    parser.add_argument("--only", help="generate only matching filename (substring match)")
    args = parser.parse_args()

    client = genai.Client(api_key=API_KEY)

    targets = IMAGES
    if args.only:
        targets = [im for im in IMAGES if args.only.lower() in im["filename"].lower()]
        if not targets:
            print(f"No images match --only '{args.only}'")
            sys.exit(1)

    print(f"\nGenerating {len(targets)} image(s) into {OUTPUT_DIR}\n")
    generated = 0
    for image_def in targets:
        if generate_one(client, image_def, force=args.force):
            generated += 1

    print(f"\nDone. {generated} image(s) generated. {len(targets) - generated} skipped.")


if __name__ == "__main__":
    main()
