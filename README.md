# The Valkorath Universe

A personal D&D-inspired worldbuilding archive — spanning multiple stories across a shared
timeline, starting with Valkorath's story, lore, and an interactive character catalog.

**A note on naming:** the stories are now titled by where they take place rather than by
their working titles — **Elarion** (formerly "Pantheon"), **Aridel** (formerly "Blade of
Honor"), and **New York** (formerly "Centennial"). Valkorath keeps its name since it's
also a place. Only the *display* names changed — the folder paths on disk and in URLs
still use the old working titles (`pantheon/`, `blade-of-honor/`, `centennial/`), so
existing links and the build script commands below are unaffected.

## What's in here

```
WorldIndex/
├── index.html               ← the universe landing page (links to all stories, in timeline order)
├── catalog/
│   └── index.html            ← Valkorath's interactive character browser
├── characters/
│   ├── catalog.json          ← all Valkorath characters, combined (used by the catalog app)
│   ├── data/                 ← one JSON file per character
│   │   └── reign-002.json
│   └── art/                  ← one portrait per character, matched by slug
│       └── reign-002.jpg
├── story/
│   └── valkorath-story.md    ← Valkorath's full narrative, chapter by chapter
├── solandis/
│   ├── catalog/index.html    ← Solandis's interactive character browser
│   ├── characters/           ← same layout as Valkorath's (catalog.json, data/, art/)
│   └── story/solandis-story.md
├── atlas/
│   ├── catalog/index.html    ← Atlas's interactive character browser
│   ├── characters/           ← same layout as Valkorath's (catalog.json, data/, art/)
│   └── story/atlas-story.md
├── neo-ciara/
│   ├── catalog/index.html    ← Neo Ciara's interactive character browser
│   ├── characters/           ← same layout as Valkorath's (catalog.json, data/, art/)
│   └── story/neo-ciara-story.md
├── pantheon/
│   ├── catalog/index.html    ← Elarion's interactive character browser
│   ├── characters/           ← same layout as Valkorath's (catalog.json, data/, art/)
│   └── story/pantheon-story.md
├── greece/
│   ├── catalog/index.html    ← Greece's interactive character browser
│   ├── characters/
│   └── story/greece-story.md
├── blade-of-honor/
│   ├── catalog/index.html    ← Aridel's interactive character browser
│   ├── characters/
│   └── story/blade-of-honor-story.md
├── london/
│   ├── catalog/index.html    ← London's interactive character browser
│   ├── characters/
│   └── story/london-story.md
├── texas/
│   ├── catalog/index.html    ← Texas's interactive character browser
│   ├── characters/
│   └── story/texas-story.md
├── centennial/
│   ├── catalog/index.html    ← New York's interactive character browser
│   ├── characters/
│   └── story/centennial-story.md
├── kryvstof/
│   ├── catalog/index.html    ← Kryvstof's interactive character browser
│   ├── characters/
│   └── story/kryvstof-story.md
└── valmere/
    ├── catalog/index.html    ← Valmere's interactive character browser
    ├── characters/
    └── story/valmere-story.md
```

All twelve stories are live now, each with a full chapter-by-chapter narrative. The landing
page (`index.html`) is the front door to the whole universe — it links out to each one in
chronological order, from Elarion's primordial age through to Neo Ciara in 2082.

The rebuild script works for any story:

```bash
python3 scripts/build_catalog.py                 # rebuilds Valkorath (default)
python3 scripts/build_catalog.py solandis         # rebuilds Solandis
python3 scripts/build_catalog.py pantheon         # rebuilds Elarion
python3 scripts/build_catalog.py greece           # rebuilds Greece
python3 scripts/build_catalog.py blade-of-honor   # rebuilds Aridel
python3 scripts/build_catalog.py atlas            # rebuilds Atlas
python3 scripts/build_catalog.py london           # rebuilds London
python3 scripts/build_catalog.py texas            # rebuilds Texas
python3 scripts/build_catalog.py centennial       # rebuilds New York
python3 scripts/build_catalog.py kryvstof         # rebuilds Kryvstof
python3 scripts/build_catalog.py valmere          # rebuilds Valmere
python3 scripts/build_catalog.py neo-ciara        # rebuilds Neo Ciara
```

## Reading chapter by chapter

Each story now has a reader alongside its catalog:

```
reader/index.html               ← Valkorath's chapter reader
pantheon/reader/index.html      ← Elarion's chapter reader
blade-of-honor/reader/index.html
centennial/reader/index.html
```

It reads the story's `.md` file directly, splits it on `## Chapter N: Title` /
`## Prologue:` / `## Epilogue:` headers, and gives you a dropdown to jump to any chapter
plus Prev/Next navigation (both a sticky top bar and buttons at the bottom of each
chapter). There's a "Read the Story →" link on every catalog page, and each reader links
back to its catalog and to the universe homepage.

Because it's driven entirely by those `## ` headers, adding a new chapter to Valkorath's
or Elarion's story file is all it takes to get it recognized -- no extra step needed.
Aridel and New York currently show up as a single "chapter" (their premise
text), since neither has a full narrative yet; once you add real chapters with `##`
headers to those `.md` files, the reader picks them up the same way.

## Faction realignment (from the character roster doc)

You provided a full character roster with definitive affiliations, and it was a big
upgrade over the story-inferred guesses from before -- **45 characters got corrected**
faction assignments as a result, including a few clear miscategorizations (Kleon was
wrongly filed under Drexl's Forces; Sir Tyrus, Sir Aldric, and Lady Valeria were wrongly
under Hidden Holy Order instead of the Valkorath Crown; Aegen and Priest David were under
Last Bastion instead of Hidden Holy Order).

New faction categories came out of this pass to match your roster's own structure:
**Sanctum of Aetheris** (Liora, Umbros, Aetheris), **Templar Order** (Baldric, Alaric,
Frenry), **Titans** (Zornath, Corthos), and **Challenge of Rights** (the 15 characters tied
to that specific trial -- Tendo, Hythm, Kazadar, Decker, Dreyfus's Hell incarnation, Moltar,
Ganador, Patchwork, Caladan, both Landis cards, Helmut, Karethos, Axeon, and Chrieser). "The
Kabal" was renamed **Black Kabal** to match your document's own terminology.

Three characters from your roster aren't in the catalog yet because there's no art or
source page for them to pull from: **Saeve** (Alexis's mother), **Silas** (Shattered Vale
rogue mage), and the cosmic overseer **Death**. If you add visual-dictionary pages for
them later, they'll slot into this same pipeline.

## About Elarion (the "pantheon" folder)

27 characters, extracted the same way as Valkorath: pulled from the visual-dictionary PDF,
cross-referenced against the actual story (28 chapters now, a complete arc — Elarion's
story reached its ending, unlike Valkorath's ongoing one).

A handful of characters had little or no bio in the source PDF (Tiavoss, Eliegh, Fleough,
Manus, Enoch) or had one that was mistakenly copy-pasted from an unrelated source (Gavinus's
bio was actually Valkorath's Reign bio, left over from an earlier draft) — those were
rewritten from scratch, grounded in what the story actually establishes about them, and
matched to the tone of the rest of the cast. Andromedus's one-line placeholder was expanded
the same way. Worth a read-through to confirm these land the way you intended.

Three characters -- Reign, Drexl, and Valerius -- share names with major Valkorath
characters. The bios note this as an intentional echo across ages without asserting exactly
how they're connected, since that's very much your call to make.

## About Aridel and New York (the "blade-of-honor" and "centennial" folders)

Both were built from PowerPoint decks rather than PDFs, but went through the same process:
character art extracted directly from the slides, bios lightly cleaned up (typos, spacing,
consistent capitalization) and organized into paragraphs, with faction and status assigned
based on what each character's own bio actually says. Nothing needed heavy invention here —
your original bios were already complete for every character in both decks.

Neither story has a chapter-by-chapter narrative yet, just the premise/setting text from
each deck's first slide — that's what's sitting in `story/blade-of-honor-story.md` and
`story/centennial-story.md`. When you write the fuller narrative for either one, drop it
into that same file and it'll read the same way Valkorath's and Elarion's do.

New York in particular pulls a lot of threads forward — Andromedus, Aetheris, Zornath,
Dreyfus, and Father Elias (Father Godskin) all reappear from earlier in the timeline, along
with Aridel's own Aluccard, Drexl Voss, and Arthur. Worth knowing if you ever want a "first
appearance" index across all four stories — that'd be a natural next feature for the
landing page.

## About Greece

A full 31-chapter story (plus prologue and epilogue), drafted from scratch based on your
character list and the "inverted history" concept -- the twist being that Rome's gods
(Jupiter, Mars, Pluto) aren't just renamed versions of the Greek Olympians, they're
parasitic reflections that grow by stealing belief from the originals, and Chronos has
braided three centuries of mortal history (Troy, the Persian invasion, Alexander's
conquests) into one compressed timeline so the Greek gods have a fighting chance to meet
that threat while they still can. Every Olympian falls a different way, on purpose:
Zeus loses despite winning his fight outright, Ares loses a duel he never needed to
accept, Hades erodes without ever being defeated, Athena is the only one who chooses her
own ending, and so on.

Three characters got added along the way that weren't on your original list, because
Troy's side of the story needed them to make sense: **Hector** (Trojan prince, Achilles's
counterpart), **Patroclus** (Achilles's companion), and **Priam** (King of Troy, Hector's
father). Flagging these clearly since they'll need art whenever you get to them -- nothing
was added without calling it out.

No character catalog data yet -- `greece/characters/` is set up and ready, but empty,
since art hasn't been made for this cast yet. The story itself is fully readable at
`greece/reader/` in the meantime. Once character art starts coming in, it'll go through
the same pipeline as everyone else: a JSON file per character in `characters/data/`, the
portrait in `characters/art/`, then `python3 scripts/build_catalog.py greece` to wire it
into the catalog.

## About Solandis

The newest addition, and the earliest story on the timeline after Elarion — a direct
prequel to Valkorath, drafted from a short outline and nine character portraits you
provided. It tells the last stand of the Templars of Solandis, a small southern kingdom
whose order of knights (the origin of the red-cross-on-white imagery later echoed by
Valkorath's own crusaders) is destroyed in a border war against Tiadel that turns out to
be a proxy for something else entirely: Lord Drexl himself, testing how much of an army he
can turn without anyone tracing it back to him.

This isn't a stand-alone story — it's built directly into existing Valkorath canon rather
than alongside it. Baldric and Alaric (Templar Order, in the main Valkorath roster) are
Solandis survivors; their existing bios already described Solandis's fall, so this story
gives that backstory its own full narrative and a little extra connective tissue was added
to both bios, plus Frenry's, tying his pyromancy back to Solandis's original flame-wielder,
Pyre. Sir Roger's death in the story's climax is also what leaves the wound on Drexl that,
years later, Sir Tyrus finally finishes in the fight his own bio already describes -- so
nothing here contradicts what was already on the site, it just fills in the gap before it.

Nine characters in `solandis/characters/`: Sigurd (the Grandmaster), Baldric and his
apprentice Alaric, Non, Pyre, Galateya, Tryfus (whose corruption is the first proof
something beyond ordinary war is at work), Sir Roger, and this era's Drexl. Portraits came
directly from the source PDF.

## A note on the modern-era stories

London, Texas, Kryvstof, and Valmere were added after this README's "About" sections were
last written and don't have write-ups here yet -- all four are live on the landing page
and fully readable, just not yet documented in this file the way the earlier stories are.

## About Atlas

A 1950s Lovecraftian noir set in a Louisiana city called Atlas, built from a short outline
and eleven character portraits. A former mafia enforcer (Bruce), a priest hiding a bad
bargain (Father Tom, formerly a sailor named Thompson), and a dragon-kin detective passing
as human (Chiro) get pulled into investigating a corruption spreading through the city, and
end up face to face with something much larger than any of them expected -- Nyarlathotep,
feeding on the city's suffering -- and are forced into a last resort that costs them the
city itself.

Like Solandis, this one is written to connect directly into characters and lore already on
the site rather than sit beside it:

- **Cthulhu** is explicitly the same being as **the Kraken** from the Greece story ("Formerly
  the kraken of the greek era of history, now cthulhu walks atlas" is straight from the
  source material) -- I added a closing line to the Kraken's existing bio in
  `greece/characters/data/kraken.json` to make the throughline explicit.
- **Dreyfus**, ruler of the underworld here, is the same Dreyfus who appears in the root
  Valkorath roster (Drexl's brother, King Dreyfus, who becomes "King of the Damned" after
  his death) and later in Centennial's New York as "Ruler of the Underworld" with a network
  of dealers called **Minodas**. Atlas is the missing middle chapter: an era before Dreyfus
  had any Minodas working for him, when he made deals like this one personally. I added
  connective notes to both `centennial/characters/data/dreyfus.json` and
  `centennial/characters/data/minodas.json` -- the latter now carries a strong implication
  that Bruce, transformed at the end of this story, is the origin of what New York's heroes
  simply know as Minodas.
- **Polygaster**, the "progenitor of the black ooze" in Atlas, is the origin point of the
  same black ooze that causes the outbreak in Kryvstof decades later. I added a line to
  `kryvstof/characters/data/zombie.json` tracing it back.
- **Chiro**'s reverence for "the great Draven" refers to Draven Blackscale, the half-dragon
  warrior from the root Valkorath roster -- a legendary ancestral figure to what's left of
  the dragon-kin by Chiro's time, rather than someone he ever met.

Eleven characters in `atlas/characters/`, portraits pulled directly from the source PDF:
Bruce, Thompson and Father Tom (his before-and-after, given separate entries the way the
site already splits other characters across life stages), Ricky, Dreyfus, Chiro, Polygaster,
Cthulhu, the Atlas-Spirit, Nyarlathotep, and Yog-Sothoth.

## About Neo Ciara

The furthest point on the timeline yet — 2082, a cyberpunk metropolis called Neo Ciara —
and by a wide margin the most heavily cross-referenced story on the site. Built from a
25-character outline, it turned out to be less a self-contained story than a converging
point for plot threads several other stories had already left open. Per your instruction,
none of the older character files this story touches were changed — every connection below
is one-directional, made only within `neo-ciara/characters/`.

The confirmed connections, all already sitting in the existing roster before this story
ever got written:

- **Kleon** ("The King Out of Time") already existed in both the root Valkorath roster and
  Centennial's New York, with a matching epithet in both places. His root bio has him
  vanishing into the timestream chasing a temporal tyrant named Gothar and never returning;
  Centennial's bio has him surfacing in 21st-century New York as a vigilante. Neo Ciara is
  simply the next stop on that same unresolved arc -- and the one where it finally resolves.
  Corthos sending him home at the end closes a loop that's been open since the root roster
  was first built.
- **Andromedus**, **Paradigm**, and **Corthos** all had existing entries (Elarion,
  Centennial, and root Valkorath respectively) establishing them as ancient, recurring,
  multi-era beings. Neo Ciara uses their established characterization directly: Andromedus's
  weariness with mortals, Paradigm's status as a 21st-century tech god, Corthos's history of
  being harvested by Malakar -- all treated as canon rather than invented fresh.
- **Malakar** and the **Vorath** curse are both established root Valkorath elements (Malakar
  as the lich who once harvested Corthos; Vorath as a corruption-title that's already been
  reused once, in London, as "the newest bearer" of an old curse). Fitch becoming "the new
  Vorath" here follows that same established pattern rather than inventing a one-off.
- **DR3-XL / Drexl Voss** is a new take on the site's most recurring name, following the
  precedent already set by Drexl's many other forms across Blade of Honor, Centennial,
  Texas, and Kryvstof -- here reincarnated, literally, inside an old robot.
- **Patchwork** is explicitly "a program designed around the psyche of the original
  Patchwork," i.e. Kryvstof's Patchwork -- the researcher who died studying the black ooze.
  Neo Ciara's version is Nexus Corp's attempt to rebuild his mind as a weapon.
- **Thor**'s existing Elarion appearance (a wandering god who passed through that realm once)
  makes his sons Magni and Modi showing up generations later, in a different story entirely,
  consistent rather than out of nowhere.

Twenty-five characters in `neo-ciara/characters/`, including several -- like Gary/Lt. Gary
and Enforcer Floret/Sgt. Floret -- split across two entries for their before-and-after life
stages, the same way Atlas split Thompson from Father Tom.

## Viewing it

Run a local server from the `Valkorath-World` folder root:

```bash
python3 -m http.server 8000
```

Then open **http://localhost:8000/** — that's the universe landing page, with a card for
each story. Click "Valkorath" to get to the character catalog.

Browsers block local file reads for security, so **don't just double-click `index.html`**
— it needs to be served, not opened directly.

(GitHub Pages will serve everything correctly once the repo is pushed, no server needed —
see below.)

## Adding or editing a character

1. Drop the portrait into `characters/art/` (jpg or png).
2. Add or edit the matching file in `characters/data/your-character-slug.json`:

```json
{
  "slug": "your-character-slug",
  "name": "Character Name",
  "epithet": "Their Title",
  "faction": "Last Bastion",
  "status": "Active",
  "tags": ["Warrior", "Leader"],
  "bio": [
    "First paragraph of their backstory.",
    "Second paragraph."
  ],
  "art": "art/your-character-slug.jpg",
  "source_page": null
}
```

3. Run the rebuild script to regenerate `catalog.json` from the individual files:

```bash
python3 scripts/build_catalog.py
```

## About the accuracy pass

119 characters total. **111 of them have now been corrected through an actual
read-through of `story/valkorath-story.md`** — faction, status (Active/Fallen/Corrupted),
and in most cases an added closing sentence grounding them in what actually happens to
them in the story. Two new factions came out of that read-through that weren't in the
original first-pass tagging: **Malakar's Legion** (Malakar operates independently of
Drexl -- the story is explicit that Drexl considers him "a nuisance," not an ally) and
**The Kabal** (a group of Drexl's former lieutenants who broke away and were later killed
by Drexl for the betrayal).

The remaining **9 characters genuinely don't appear in the story text at all** (checked
directly, not assumed): Calador, Dark Reign, Gothar, Kleon, Lucan, Lumbar, Nyx, Ouken, and
Vornath. They're visual-dictionary-only characters for now -- their original first-pass
tags are left as a placeholder, since there's nothing in the narrative yet to correct them
against.

One naming bug was also fixed: the character on visual-dictionary page 59 was mislabeled
"Kandor" in the page header even though the bio is entirely about a character named
**Alexis** -- corrected to Alexis. The story's actual Kandor (a displaced knight from King
Valerius II's era, original wielder of the sword Thunderstrike) is a different, separate
character on page 84, and was left as-is.

Worth knowing: an early automated attempt at this pass (matching faction/status by simple
keyword proximity to a character's name) produced confidently wrong answers -- e.g. it
nearly tagged David, a Last Bastion founder, as one of Drexl's own forces, simply because
Drexl's name appears near his often in battle scenes. That approach was discarded entirely
in favor of actually reading the relevant passages for each character.

A few characters still lack the multi-paragraph bios their peers have (pages that were
mostly illustration in the source PDF, with little to no body text) -- those are flagged
for a manual fill-in.

## Keeping this private

This repo is meant to stay **private** while the world is in progress:

- On GitHub: create the repo as **Private** (Settings → visibility, or choose Private at
  creation). Private repos are free and unlimited on GitHub's free tier.
- If you ever turn on **GitHub Pages** to host the catalog as a real website: on a free
  GitHub plan, Pages sites are public even if the repo is private. If you want the hosted
  version to stay private too, you'd need GitHub Pages' private-Pages support, which
  requires a paid plan (Pro/Team/Enterprise) — otherwise just keep using the local-server
  method above, which stays fully private with a free account.

## The story

`story/valkorath-story.md` has the full narrative, organized by chapter with Markdown
headers (`## Chapter N: Title`) so it renders cleanly on GitHub or in any Markdown viewer.
