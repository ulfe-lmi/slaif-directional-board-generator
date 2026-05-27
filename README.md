<div style="text-align: center;">
  <a href="https://www.slaif.si">
    <img src="https://slaif.si/img/logos/SLAIF_logo_ANG_barve.svg" width="400" height="400">
  </a>
</div>

# SLAIF Directional Board Generator

This project defines a small workflow for producing printable directional
boards for SLAIF events. The output is always a single eight-page PDF, with
one page for each required arrow direction.

The boards are intended for real event signage, so the design priorities are
clarity, readability, and consistency. Each page uses the same board design:
the SLAIF logo, the event title, and one large directional arrow. Only the
arrow direction changes from page to page.

## What It Produces

For each event, the generator produces one print-ready PDF containing exactly
eight A4 pages:

1. Up
2. Right
3. Left
4. Down
5. Up-right
6. Down-right
7. Down-left
8. Up-left

The page orientation can be either landscape or portrait, depending on the
event need. A thin rounded border can also be included when requested.

## Required Inputs

Before generating boards, the workflow needs three pieces of information:

- Event title: the exact title printed on every board.
- Orientation: `landscape` or `portrait`.
- Border preference: whether to include a rounded border.

The expected input format is:

```text
Title: <event title>
Orientation: landscape or portrait
Border: yes or no
```

## Source Asset

The SLAIF logo is expected to be present as `logo.svg` in the project root.
The logo should be used directly from that SVG file so the official mark is
preserved. The palette should also be extracted from the SVG and reused for
the board colors, especially the green used for the title and arrow.

## Design Approach

The design should be created once and reused across all eight pages. This
keeps the signage set consistent and avoids each direction looking like a
separate design.

For landscape boards, the preferred composition is:

- A large centered event title in the upper third of the page.
- The SLAIF logo placed large in the lower-left area.
- A large directional arrow placed in the lower-right area.
- Enough whitespace around the title, logo, arrow, border, and page edges.

For portrait boards, a top-to-bottom layout is usually more appropriate:

- Logo near the top.
- Title below the logo or near the middle.
- Large arrow in the lower part of the page.

The arrow should be one of the green colors from the SLAIF logo palette and
should never be gray. The title should use a clean bold font and remain
readable from a distance.

## Verification

After generating the PDF, all eight pages should be rendered to images and
visually inspected before the result is delivered. The verification pass should
confirm that:

- The PDF has exactly eight pages.
- Every page is nonblank.
- The logo renders correctly and is not distorted.
- The event title is present, readable, and not crowded.
- The arrow is large, clear, and present in each required direction once.
- All pages share the same design and differ only by arrow direction.
- Nothing overlaps or sits too close to the page edges or optional border.

If any rendered page fails inspection, the layout should be adjusted and the
PDF regenerated before delivery.
