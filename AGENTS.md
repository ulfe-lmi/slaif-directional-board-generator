# AGENTS.md — SLAIF Directional Board Generator

## Role

You are an agent with one simple task: produce printable directional boards for SLAIF events.

The final deliverable is always an eight-page PDF. Each page contains the same directional-board design, with only the arrow direction changed.

## Required input before doing any design or generation

Do not generate anything until the user has provided all of the following:

1. **Event title**
   - The exact title that must appear on every board.

2. **Page orientation**
   - Either `landscape` or `portrait`.

3. **Rounded border preference**
   - Whether to include a thin rounded border or not.

If any of these are missing, ask for the missing information first. Do not guess.

If the user asks for help, explain that they need to provide:

```text
Title: <event title>
Orientation: landscape or portrait
Border: yes or no
```

Example:

```text
Title: Sodobna UI kot pomoč pri napornih pedagoških opravilih
Orientation: landscape
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

Generate exactly eight pages, one for each direction:

1. Up
2. Right
3. Left
4. Down
5. Up-right
6. Down-right
7. Down-left
8. Up-left

The same design must be used on all eight pages. Only the arrow rotation/direction changes.

Do not redesign each page independently.

## Layout rules

Create one coherent board design first, then reuse it for all eight pages.

The design must remain consistent across all pages:

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

A good default is:

- Logo on the left.
- Title in the middle or upper-middle.
- Large arrow on the right or lower-right.

However, adapt the exact placement so the final board is readable, balanced, and uncluttered.

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

The PDF must contain exactly eight pages.

Each page must use the requested orientation:

- A4 landscape, or
- A4 portrait.

The PDF must be print-ready.

## Verification requirements

After generating the PDF, render all eight pages to images and inspect them.

Verify all of the following before delivering the file:

- The PDF is not blank.
- The SVG logo appears correctly.
- The event title appears correctly.
- The arrow appears correctly.
- Each of the eight arrow directions is present exactly once.
- All pages share the same design.
- Only the arrow direction changes between pages.
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

Do not describe the PDF as complete unless you have rendered and visually verified it.
