# My Town style guide

Claude's rules for keeping every screen of My Town looking like one game. Set Nov 19, 2026. The Dress Up doll and clothing set the look: soft, flat, friendly, with no thick outlines.

**How activities work** (dragging tools, how much rubbing finishes a step, timing, pacing, Thanks and money cards, sounds): see [activity-rules.md](activity-rules.md). The Vet Clinic is the standard for every building (Mac, Nov 25, 2026).

## The look in one line
Soft children's illustration with flat, bright colors (soft, not faded), rounded shapes, no outer outlines, and depth from soft shadows a little darker than the color they sit on. Everything is matte, with no shine, glow or 3D look.

## Shapes and icons (drawn in code)
- Filled shapes only. No outline around the outside of anything: the edge is just the color meeting the background.
- Two tones per part: the main color, plus one soft shadow shape about 12% darker on the lower or inner side. One small lighter spot at most, for a highlight.
- Inside detail lines (seams, doors, pockets) are the part's color about 20% darker, thin, with rounded ends. Never black, gray or brown unless that is the part's color.
- Corners and ends are rounded. Icons read at 40 px and have no words.
- On colored buttons (like the tabs and dice), small icons are one color (white or the text color) so they stay easy to read.

## Colors (one small set, Nov 23, 2026)
Use only these. If a new thing needs a color, pick from this list instead of adding a new hue.
- **Ink:** plum `#4a3b5c` for all words (titles, directions, labels on light backgrounds); soft plum `#6b5a80` for less important words.
- **Surfaces:** white `#ffffff`, cream `#fffaf5`, lavender tint `#f3edf8`, pink tint `#ffe8f0`.
- **Five button colors**, each with a pressed edge about 20% darker:
  - Berry pink `#e0457b` / `#b8336a`: going back to town, the Boutique.
  - Leaf green `#5fae7a` / `#468a5e`: go, done, success, and the Vet Clinic.
  - Sky blue `#4a9be0` / `#3479b8`: undo, next page, water, a boy.
  - Sunny yellow `#ffc94d` / `#d9a531`: the dice, stars and sparkles (icons on yellow are plum or white).
  - Charcoal gray `#5f5a6b` / `#46424f`: clear, close, back inside a panel.
- **Purple `#7b5cd6`** is only for the chosen tab in Dress Up (not for buttons).
- **Building colors** stay the same everywhere (map, room walls, buttons): Boutique pink, Department Store teal walls with a deeper teal roof (recolored from yellow Nov 25, 2026) and cream trim; its room inside is soft lavender with white trim, a pale honey floor and a coral rug (Mac picked it Nov 25, 2026, so it looks different from the pink Boutique and mint Vet Clinic rooms), Vet Clinic mint walls with a green roof, General Store pale yellow and brown, Library lavender and purple. A building's own color is used only for its buttons and title, and must be one of the five button colors when it is a button.
- **Cars and other moving things** use the five button colors plus cream and light sky `#a9d3f5`, never neon.
- **Greens (Nov 23, 2026): three, all taken from the Vet Clinic's own pictures.** Light mint `#bae5ca` (the wall; its pale version `#e5f4ea` for big card backgrounds), soft leaf `#5fae7a` with pressed edge `#468a5e` (every green button, arrow, border and title), and forest `#3e6e4b` (green words). No other greens in buttons, words or backgrounds. Clothing and pictures keep their own colors. Words that are not current or not important use soft plum, not gray-green.
- **Highlights:** soft yellow ring `#fff6b0`. Done things never light up again.
- **The town icon** is the same picture everywhere: a pink house and a sky blue house with a yellow roof (no green), on a white badge inside colored buttons.

## Words
- Easy words for Pre-K to 3rd grade, as few as possible: the checklist and highlights already say what to do.
- Periods, not exclamation points. Save "!" for celebrations ("Just right!", "Great job!", "All done!").
- Tasks are actions: Pick a pet, Weigh, Food, Bath (never a result like "16 lb").
- **Three kinds of text look different:**
  - Labels (names of places, like Dogs or Food): small white pill with a brown edge `#8a5a3b`, brown words.
  - Directions (what to do next): a soft cream bubble with no edge, a soft shadow, and plum words.
  - Buttons: a solid color with white words and a pressed edge (see Buttons).

## Arrows (Nov 25, 2026)
- Every arrow has depth, like the town's pick arrow: a thick rounded block arrow in one color, a copy about 20% darker just under it (7 units lower), and one small light streak on top. No flat line arrows.
- An arrow that points at something outside a card (like the toolbar) sits outside the card, right next to the thing, and bobs toward it.

## Pop-up messages (Nov 25, 2026)
- One look everywhere (the Vet Clinic's "Your backpack is empty" box): a white box at the top center, dark words `#2b2340`, bold Verdana, 14 px corners, soft shadow, no border. Long messages wrap.
- Players are learning to read: a message stays up at least 4.5 seconds, plus about a tenth of a second per letter (`tbReadMs` in the toolbar). Never a quick flash.

## Dragging (Nov 23, 2026)
- Close enough counts: a drop works within about 45 room units of the target (more room below for things that sit on the floor).
- Things snap into place and the action starts as soon as they get there, without letting go (the water bowl filling at the sink is the model).
- A wrong drop slides back home. Never stop the player in the middle of a drag before they have had at least 3 more seconds.

## Buttons (raised pop-outs)
- Rounded (14 to 20 px corners), no border line. Every button in every game uses this style (Dress Up's trash and All Done are the model).
- Raised: a solid bottom edge `0 4px 0` in the darker shade, plus a soft drop shadow `0 8px 18px rgba(74, 59, 92, .15)`.
- Press: moves down 3 to 4 px and the edge shrinks to 1 px.
- Hover or focus: the icon lifts 2 to 3 px and tilts a little.
- At least 44 px tall and wide (48 or more for main buttons). Icons first; a word under an icon is fine for tabs.
- Off or not ready yet: faded to 35% with no edge, or a small lock badge.

## Panels and bars
- White or cream, 22 to 26 px corners, no border line, with a soft shadow `0 10px 30px rgba(120, 60, 120, .15)` and a faint lavender rim `0 0 0 2px #f3edf8`.
- Pop-ups grow from the button that opened them (a scale bounce), and close by tapping anywhere else.
- Task bars (Mac, Nov 25, 2026): always stretch all the way across the top, edge to edge, even with only a few steps. Never centered. Logo, name and divider sit at the left and the steps follow from the left; any space left over stays on the right. The Vet Clinic game after you pick a pet is the example. Back to town sits above the task bar at the top left (on short screens, inside the bar's left end). A town room with a task bar uses the same frame, size and spot as its game screen, so nothing moves when you go in. Every building's room has a task bar with its logo and name (Mac, Nov 26, 2026); see activity-rules.md, Opening a building.

## Motion
- Feedback is quick (0.2 to 0.6 s): a bounce in (`cubic-bezier(.3, 1.5, .5, 1)`), a squash when landing, a wiggle for "not yet", and sparkles in pink, purple, green, blue and yellow.
- Steady motion is gentle and in the scene, not on the buttons: cars, clouds, the fountain, swaying trees, sparkles on what you can tap.
- Characters in boxes stay still. Only the moment something new arrives gets motion (the sticker stamp).
- Always respect reduced motion.

## Screens
- Scenes (map, rooms) fill the whole screen, with no title bar or instruction text.
- The toolbar sits in the bottom right corner of every screen. Scenes keep tap targets out of that corner, and pages leave room under their own buttons for it.
- The Back button (top left) has the arrow, the town icon and the words "Back to town", and always goes to the town map. On small screens only the arrow and icon show.
- Text is Verdana, bold for buttons, and kept to a minimum: icons first, for emerging readers.
- Pictures from Gemini: match the Boutique building (Mac, Nov 22, 2026): no dark outlines, soft clay-like rounded shapes, a thick soft roof, low detail. Check every new picture with the town-style-check skill before adding it. Everything Claude draws on top follows this guide.

## Sounds
Short Web Audio tones: rising notes for good things, two falling soft notes for "not yet".
