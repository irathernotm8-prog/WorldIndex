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
Valkorath-World/
├── index.html               ← the universe landing page (links to all stories)
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
├── pantheon/
│   ├── catalog/index.html    ← Elarion's interactive character browser
│   ├── characters/           ← same layout as Valkorath's (catalog.json, data/, art/)
│   └── story/pantheon-story.md
├── blade-of-honor/
│   ├── catalog/index.html    ← Aridel's interactive character browser
│   ├── characters/
│   └── story/blade-of-honor-story.md
├── centennial/
│   ├── catalog/index.html    ← New York's interactive character browser
│   ├── characters/
│   └── story/centennial-story.md
└── greece/
    ├── catalog/index.html    ← Greece's interactive character browser
    ├── characters/           ← currently empty, awaiting character art
    └── story/greece-story.md
```

All five stories are live now. The landing page (`index.html`) is the front door to the
whole universe — it links out to each one.

The rebuild script works for any story:

```bash
python3 scripts/build_catalog.py                 # rebuilds Valkorath (default)
python3 scripts/build_catalog.py pantheon         # rebuilds Elarion
python3 scripts/build_catalog.py blade-of-honor   # rebuilds Aridel
python3 scripts/build_catalog.py centennial       # rebuilds New York
python3 scripts/build_catalog.py greece           # rebuilds Greece
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
