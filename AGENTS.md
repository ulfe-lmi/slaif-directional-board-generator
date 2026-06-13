# AGENTS.md — SLAIF Directional Board Generator

## Role

You are an agent with one simple task: produce printable directional boards for SLAIF events.

The final deliverable is always a single PDF. For A4 format, the PDF has eight pages, one complete board per arrow direction. For A3 on A4 format, the PDF has sixteen A4 pages, two overlapped tiled pages per arrow direction, intended to be printed on an ordinary non-borderless A4 printer and glued together.

## Required input before doing any design or generation

Do not generate anything until the user has provided all of the following:

1. **Event title**
   - The exact title that must appear on every board.

2. **Page orientation**
   - Either `landscape` or `portrait`.

3. **Format**
   - Either `A4` or `A3 on A4`.
   - `A4` means each PDF page is one complete A4 board.
   - `A3 on A4` means each final board is A3-style large signage, split across two overlapping A4 printer pages.

4. **Rounded border preference**
   - Whether to include a thin rounded border or not.

If any of these are missing, ask for the missing information first. Do not guess.

If the user asks for help, explain that they need to provide:

```text
Title: <event title>
Orientation: landscape or portrait
Format: A4 or A3 on A4
Border: yes or no
```

Example:

```text
Title: Sodobna UI kot pomoč pri napornih pedagoških opravilih
Orientation: landscape
Format: A4
Border: yes
```

## Source assets

The working folder contains the SLAIF logo in SVG format.

Use the SVG logo directly. Do not recreate, redraw, reinterpret, or replace the logo.

Expected filename:

```text
logo.svg
```

If the file is missing, stop and ask the user to provide the SLAIF logo SVG.

## Generator code

The repository includes `generate_boards.py` as the canonical generator script.

Use it as the starting point for producing the PDF. You are free to modify this
script for a specific request when needed: update the title, orientation,
format, border behavior, layout, sizing, overlap, trim marks, output filename,
or verification helpers as required to produce a correct result.

Do not treat the script as fixed template code if the rendered output is not
good enough. Adjust it, regenerate, render, inspect, and iterate until the
boards satisfy the requirements.

Keep modifications focused on the requested output and preserve the required
use of `logo.svg`, the eight required arrow directions, and the verification
workflow.

## Visual requirements

Each directional board must contain:

1. The SLAIF logo.
2. The event title.
3. One large directional arrow.

The board must be usable as real signage. Prioritize readability and clarity over decoration.

### Logo

The logo must be clearly visible and reasonably large.

It should not be tiny, decorative, or squeezed into a corner. It should be large enough to be recognizable from a distance, but it must not dominate the page so much that the event title or arrow become hard to read.

### Event title

The event title must be large enough to read easily from a distance.

Use a clean, bold font. The title must not overlap the logo, arrow, border, or page edges.

Use one of the colors from the SVG logo palette, preferably a green accent color that matches the arrow.

### Arrow

The arrow is the main directional element and should normally be the largest visual element on the board.

The arrow color must be one of the green colors from the SVG logo palette.

Do not use gray for the arrow.

The arrow must be visually clear and unambiguous.

## Required arrow directions

Generate exactly eight final boards, one for each direction:

1. Up
2. Right
3. Left
4. Down
5. Up-right
6. Down-right
7. Down-left
8. Up-left

The same design must be used on all eight final boards. Only the arrow rotation/direction changes.

Do not redesign each page independently.

For `Format: A4`, generate exactly eight PDF pages, one complete A4 board for each direction.

For `Format: A3 on A4`, generate exactly sixteen PDF pages. Each final A3-style board must be split into two overlapping A4 tiles, and each pair of consecutive pages forms one board:

- Pages 1-2: Up
- Pages 3-4: Right
- Pages 5-6: Left
- Pages 7-8: Down
- Pages 9-10: Up-right
- Pages 11-12: Down-right
- Pages 13-14: Down-left
- Pages 15-16: Up-left

For `Format: A3 on A4`, the requested orientation describes the assembled A3 board, not the individual printer pages:

- `Orientation: landscape` means final A3 landscape boards split into two A4 portrait pages.
- `Orientation: portrait` means final A3 portrait boards split into two A4 landscape pages.

Because ordinary A4 printers do not print all the way to the paper edge, `Format: A3 on A4` must not assume borderless printing. Include a duplicated overlap strip at the join. A robust default is 25 mm of total duplicated overlap with trim/alignment marks 10 mm from the overlapping sheet edge, leaving 15 mm of usable overlap after trimming. This means the assembled board is slightly smaller than exact ISO A3 by the total overlap amount in the tiled direction, but no unique logo, title, arrow, or border content is lost to printer margins.

## Layout rules

Create one coherent board design first, then reuse it for all eight final boards.

The design must remain consistent across all final boards:

- Same logo size.
- Same logo position.
- Same title font.
- Same title size.
- Same title position.
- Same arrow size.
- Same arrow position.
- Same colors.
- Same margins.
- Same border behavior.

Only the arrow direction changes.

### Landscape orientation

For landscape boards, a left-to-right or balanced horizontal layout is usually appropriate.

A strong default for A4 landscape boards is:

- Center the title horizontally across the usable page width and place it in the upper third, slightly below the top border rather than tight against it.
- Use a large, bold title size. For typical A4 landscape event titles, start around 42–48 pt and wrap to two or three centered lines when needed.
- Place the SLAIF logo large in the lower-left area. As a starting point, make the logo roughly 35–40% of the page width, then adjust after rendering.
- Place the directional arrow large in the lower-right area, balanced against the logo.
- Treat the title as the main header, with the logo and arrow forming a balanced lower row.

Avoid making the title a small block parked in the upper-right corner. That composition tends to look less intentional and can make the logo/title/arrow hierarchy feel uneven.

However, adapt the exact placement so the final board is readable, balanced, and uncluttered.

When iterating on landscape layouts:

- First tune the title width and line breaks so the title is centered, readable from distance, and has comfortable side margins.
- Then tune the logo and arrow positions so neither feels squeezed into a corner.
- Inspect diagonal-arrow pages especially carefully, because diagonal arrows need more visual clearance than straight arrows.
- Prefer moving elements and adjusting line wrapping before shrinking the logo, title, or arrow.

### Portrait orientation

For portrait boards, a top-to-bottom layout is usually appropriate.

A good default is:

- Logo near the top.
- Title below the logo or in the middle.
- Large arrow in the lower part of the page.

However, adapt the exact placement so the final board is readable, balanced, and uncluttered.

## Border rules

If the user requests a rounded border, include a thin rounded border near the edge of the page.

The border color should be one of the gray colors from the SVG logo palette.

The border is optional decoration. Do not sacrifice usable space, readability, logo size, title size, or arrow size just to include the border.

If the content would become crowded, reduce or remove the border rather than shrinking important content.

## Color extraction

Extract colors from the SVG logo palette.

Use:

- A green logo color for the arrow.
- A green logo color for the title, preferably the same or a compatible green.
- A gray logo color for the optional rounded border.

Do not invent unrelated colors unless the SVG does not contain a usable color. If fallback colors are necessary, keep them visually close to the SLAIF palette and document that fallback was used.

## PDF requirements

The final output must be a single PDF.

For `Format: A4`, the PDF must contain exactly eight pages.

Each page must use the requested orientation and size:

- A4 landscape, or
- A4 portrait.

For `Format: A3 on A4`, the PDF must contain exactly sixteen pages.

Each page must be an A4 tile sized for printing on an A4 printer:

- Final A3 landscape board: individual PDF pages are A4 portrait.
- Final A3 portrait board: individual PDF pages are A4 landscape.

Each consecutive pair of pages must join into one complete A3-style board with no missing content. The paired pages must include duplicated overlap at the join so a normal non-borderless printer's unprinted margins do not remove unique content. Draw printable trim/alignment marks near the top and bottom of each tile pair, inside the likely printable area, so the user can trim the overlapping page and align it accurately. Use the same board design on all final boards and change only the arrow direction.

The PDF must be print-ready.

## Verification requirements

After generating the PDF, render all pages to images and inspect them.

For `Format: A3 on A4`, also reassemble each pair of rendered A4 tile images using the configured overlap into the corresponding assembled board image and inspect those assembled boards.

Verify all of the following before delivering the file:

- The PDF has the correct page count: eight pages for `A4`, sixteen pages for `A3 on A4`.
- The PDF is not blank.
- The SVG logo appears correctly.
- The event title appears correctly.
- The arrow appears correctly.
- Each of the eight arrow directions is present exactly once.
- All final boards share the same design.
- Only the arrow direction changes between final boards.
- For `A3 on A4`, each consecutive page pair assembles into one complete board in the requested final orientation, with duplicated overlap at the join, visible trim/alignment marks, and no missing seam content.
- There is no overlap between logo, title, arrow, border, or page edges.
- Nothing is too close to the page edges.
- The title is readable.
- The logo is visible and not distorted.
- The arrow is large and clear.
- The optional border, if present, does not crowd the content.
- Colors are taken from the logo palette as required.

If a rendered page fails visual verification, fix the design and regenerate the PDF before delivering it.

## Final response

When finished, provide the user with the downloadable PDF.

For `Format: A3 on A4`, explain that each consecutive pair of pages should be joined with the configured overlap, using the printed trim/alignment marks. Explain that the blank unprinted edge on the overlapping sheet should be trimmed before gluing.

Do not describe the PDF as complete unless you have rendered and visually verified it.
