# House style for this lecture series

Every lecture in this repo follows the same rules, so that the decks look and read as one series. Use `slides/_template.html` to start a new deck.

## Adding a lecture

1. Copy `slides/_template.html` to `slides/NN-slug.html` (two-digit number, short slug).
2. Add any new labs to `widgets/`. Labs are numbered across the whole series (Lab 1, Lab 2, ... in order of first use).
3. Add `lectures/NN-slug.html`, modelled on an existing lecture page: a card for the slides, one card per lab, and a "What the lecture covers" list.
4. Add the lecture to the list on `index.html` and its objectives to `README.md`.
5. Topic sessions, which are not tied to a place in the sequence, drop the number: `slides/slug.html` and `lectures/slug.html`, with the kicker `Epidemiological Thinking · Topic name`. They are listed under "Topic sessions" on `index.html`.
6. Run the checker (below) until it reports `all clean`, then look at every slide and lab in light mode, dark mode and at phone width.

## Slides

- reveal.js, 1280 by 720, styles from `assets/css/tokens.css` and `assets/css/slides.css`. Use the existing classes (`.lede`, `.claim`, `.claim.good`, `.claim.warn`, `.cards`, `.card`, `.stat`, `.eq`, `.frac`, `.pill`, `.cite`, `ol.sources`). Anything a deck needs beyond these, such as a chart, goes in that deck's own `<style>` block.
- Every slide title is a claim or a question, not a topic label. "Counts mislead. Divide by the number at risk", not "Rates".
- One idea per slide.
- When the room should think, put the question on one slide and the answer on the next.
- Every slide has speaker notes (`<aside class="notes">`), written as what the teacher would say.
- Text never smaller than 14 pt (19 px on the slide).
- No em dashes anywhere, including notes.
- Plain English: short sentences, define a term the first time it is used.
- Colours carry meaning: navy for the main series and claims, green for what works or resolves, amber for caution or a trap, red only for reject or harm.
- Real data wherever possible, cited on the slide (`.cite`) and in the sources slide. Any made-up example is labelled "Illustrative, constructed for teaching".
- The cover kicker reads `Epidemiological Thinking · Lecture N` (or `Epidemiological Thinking · Topic name` for a topic session). No personal names on any visible page; credit AIIMS Bhopal.

## Labs

- One self-contained HTML page each in `widgets/`, using `widget.css` and `theme.js` (light by default, Dark/Light toggle).
- Every lab works on a phone and supports `?embed=1`, which hides the header and footer so it can sit in a slide inside an `iframe.lab`. Keep the most important view within 1152 by 536 px in embed mode.
- Presets come from published sources, named on the page.

## Checks

```
python3 -m http.server 8765 &
npm install            # once, for playwright-core
node src/chk.mjs NN-slug
```

The checker reports overflow past the slide, text under 14 pt, missing notes, em dashes and JS errors.

`python3 src/bundle.py [site_url]` writes single-file copies of every deck and lab to `dist/` for sharing offline.
