---
name: slaif-directional-boards
description: Generate printable SLAIF event directional-board PDFs from the required title, orientation, format, and border inputs. Use when Codex is asked to create SLAIF signage, directional boards, arrow signs, A4 board PDFs, or A3 boards tiled for printing on A4 paper.
---

# SLAIF Directional Boards

Produce one print-ready PDF of SLAIF directional boards. Use the project `logo.svg` directly, extract colors from that SVG palette, and verify rendered output before delivery.

Use `generate_boards.py` as the canonical generator script in this repository.
Modify it freely for the current request when needed: title, orientation,
format, border behavior, layout, sizing, overlap, trim marks, output filename,
or verification helpers. Do not keep a bad rendered result just because the
existing script produced it. Adjust the code, regenerate, render, inspect, and
iterate until the PDF is ready to hand over.

## Required Inputs

Do not generate anything until the user provides all four inputs:

```text
Title: <event title>
Orientation: landscape or portrait
Format: A4 or A3 on A4
Border: yes or no
```

If anything is missing, ask only for the missing values.

`Format: A4` means eight complete A4 boards, one board per PDF page.

`Format: A3 on A4` means eight final A3-style boards tiled for an ordinary non-borderless A4 printer, two overlapping A4 pages per board, sixteen PDF pages total.

For `A3 on A4`, the requested orientation describes the final assembled A3 board:

- `landscape`: split each A3 landscape board into two A4 portrait pages.
- `portrait`: split each A3 portrait board into two A4 landscape pages.

For `A3 on A4`, include a duplicated overlap strip at the join. Do not assume borderless printing. A robust default is 25 mm of total duplicated overlap with trim/alignment marks 10 mm from the overlapping sheet edge, leaving 15 mm of usable overlap after trimming. The assembled board is slightly smaller than exact ISO A3 by the total overlap amount in the tiled direction, but unique logo, title, arrow, and border content must not be lost to printer margins.

## Board Set

Generate exactly eight final boards in this order:

1. Up
2. Right
3. Left
4. Down
5. Up-right
6. Down-right
7. Down-left
8. Up-left

Use one coherent board design for all directions. Keep logo size, logo position, title font, title size, title position, arrow size, arrow position, colors, margins, and border behavior identical. Change only the arrow direction.

For `A3 on A4`, pair pages consecutively:

- Pages 1-2: Up
- Pages 3-4: Right
- Pages 5-6: Left
- Pages 7-8: Down
- Pages 9-10: Up-right
- Pages 11-12: Down-right
- Pages 13-14: Down-left
- Pages 15-16: Up-left

## Visual Rules

Include the SLAIF logo, the event title, and one large directional arrow on every final board.

Use the SVG logo directly from `logo.svg`. Do not recreate, redraw, reinterpret, or replace it. If `logo.svg` is missing, stop and ask the user to provide it.

Use a clean bold font for the title. Keep the title large, readable, and clear of the logo, arrow, border, and edges.

Use green colors from the SVG logo palette for the title and arrow. Do not use gray for the arrow. Use a gray from the logo palette for the optional rounded border.

If `Border: yes`, include a thin rounded border near the final board edge. Do not let the border crowd the content.

For landscape boards, prefer a balanced horizontal layout with the logo on the left, title in the middle or upper-middle, and arrow on the right or lower-right.

For portrait boards, prefer a top-to-bottom layout with the logo near the top, title below or in the middle, and arrow in the lower part.

## Verification

Render every PDF page to an image before delivery.

For `A4`, inspect all eight rendered pages.

For `A3 on A4`, inspect all sixteen rendered A4 pages and reassemble each consecutive page pair into an assembled board image using the configured overlap.

Verify:

- Correct page count: eight for `A4`, sixteen for `A3 on A4`.
- Correct page size and orientation.
- Nonblank pages.
- SVG logo appears correctly and is not distorted.
- Event title appears correctly and is readable.
- Arrow appears clearly and each required direction appears exactly once.
- Final boards share the same design, with only arrow direction changing.
- For `A3 on A4`, each page pair assembles into one complete board with duplicated overlap at the join, visible trim/alignment marks, and no missing seam content.
- No overlaps between logo, title, arrow, border, or page edges.
- Nothing is too close to edges.
- Colors are taken from the logo palette.

Fix failures and regenerate before delivering the PDF.

For `A3 on A4`, tell the user to join each consecutive page pair with the configured overlap using the printed trim/alignment marks. Mention that the blank unprinted edge on the overlapping sheet should be trimmed before gluing.
