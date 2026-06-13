<div style="text-align: center;">
  <a href="https://www.slaif.si">
    <img src="https://slaif.si/img/logos/SLAIF_logo_ANG_barve.svg" width="400" height="400">
  </a>
</div>

# SLAIF Directional Board Generator

This repository is operated through a coding agent. It is not intended as a
manual end-user tool.

The user provides the event parameters. The coding agent updates or runs the
generator, creates the PDF, renders the PDF pages to images, visually inspects
the result, fixes layout problems, regenerates as needed, and only then hands
over the final PDF.

## User Request Format

Before generating anything, the coding agent must have all four values:

```text
Title: <event title>
Orientation: landscape or portrait
Format: A4 or A3 on A4
Border: yes or no
```

Example:

```text
Title: Delavnica Orkestrirano agentno programiranje
Orientation: landscape
Format: A3 on A4
Border: yes
```

If any value is missing, the agent asks only for the missing value. It must not
guess.

## Output Modes

The final deliverable is always one PDF.

### A4

`Format: A4` creates 8 PDF pages. Each page is one complete A4 board.

The requested orientation is the orientation of each PDF page:

- `landscape`: A4 landscape pages
- `portrait`: A4 portrait pages

### A3 on A4

`Format: A3 on A4` creates 16 PDF pages. Each final board is split across two
A4 printer pages.

The requested orientation is the orientation of the assembled board:

- `landscape`: final large landscape board, split into two A4 portrait pages
- `portrait`: final large portrait board, split into two A4 landscape pages

The two pages in each pair must include duplicated overlap and printable
trim/alignment marks. This is required because ordinary A4 printers do not
print all the way to the paper edge. A plain two-page split loses content at
the join.

A robust default is:

- 25 mm total duplicated overlap
- trim/alignment marks 10 mm from the overlapping sheet edge
- 15 mm usable overlap after trimming

The assembled board is slightly smaller than exact ISO A3 in the tiled
direction. That is intentional and preferable to missing seam content.

## Required Board Set

Generate exactly eight final boards, in this order:

1. Up
2. Right
3. Left
4. Down
5. Up-right
6. Down-right
7. Down-left
8. Up-left

The design must be identical across all final boards. Only the arrow direction
changes.

For `A3 on A4`, the page pairs are:

- pages 1-2: Up
- pages 3-4: Right
- pages 5-6: Left
- pages 7-8: Down
- pages 9-10: Up-right
- pages 11-12: Down-right
- pages 13-14: Down-left
- pages 15-16: Up-left

## Source Asset

The repository must contain:

```text
logo.svg
```

The agent must use this SVG directly. It must not redraw, reinterpret, replace,
or convert the logo unless that is explicitly required for a technical fix.

The board colors should be extracted from the SVG palette:

- green from the logo for the title
- green from the logo for the arrow
- gray from the logo for the optional rounded border

## Visual Requirements

Each final board must contain:

- the SLAIF logo
- the event title
- one large directional arrow

The sign must be readable from a distance. Prioritize clarity over decoration.

The logo must be clearly visible and not distorted.

The title must be large, bold, readable, and clear of the logo, arrow, border,
and page edges.

The arrow should normally be the largest visual element. It must be green, not
gray, and the direction must be unambiguous.

If `Border: yes`, include a thin rounded gray border. The border must not crowd
the content.

## Agent Workflow

The coding agent should follow this workflow for every generation request.

### 1. Confirm Inputs

Confirm the request includes:

```text
Title
Orientation
Format
Border
```

Stop and ask for missing values before editing or generating anything.

### 2. Inspect the Workspace

Check that `logo.svg` exists.

Read the current generator and instructions before editing:

```bash
rg --files
sed -n '1,260p' generate_boards.py
sed -n '1,260p' AGENTS.md
```

### 3. Generate the PDF

The implementation may use the existing `generate_boards.py` or another
appropriate script, but the output must follow the rules in this README and
`AGENTS.md`.

The generated PDF should go under:

```text
dist/
```

`dist/` is generated output and is normally not committed.

`generate_boards.py` is the canonical generator script in this repository. The
agent is expected to modify it when needed for the requested title, format,
orientation, border, layout, overlap, trim marks, or output filename. The script
is a working starting point, not an untouchable template.

### 4. Verify Metadata

Use `pdfinfo` or an equivalent tool.

For `A4`, verify:

```text
Pages: 8
Page size: A4 in the requested orientation
```

For `A3 on A4`, verify:

```text
Pages: 16
Page size: A4 in the required tile orientation
```

### 5. Render Every Page

Render the PDF pages to images, for example:

```bash
mkdir -p dist/rendered-check
pdftoppm -png -r 120 path/to/output.pdf dist/rendered-check/page
```

The agent must inspect the rendered images before delivery.

### 6. Reassemble Tiled Boards

For `A3 on A4`, the agent must also reassemble each rendered page pair into
the final board image using the configured trim/overlap values.

Inspect the reassembled board images, not only the individual tiles.

### 7. Visual Inspection Checklist

Before handing over the PDF, verify:

- the PDF is not blank
- the PDF has the correct page count
- the SVG logo appears correctly
- the logo is visible and not distorted
- the event title appears correctly
- the title is readable from a distance
- the arrow appears clearly
- all eight required arrow directions are present exactly once
- the design is consistent across all final boards
- only the arrow direction changes
- no logo, title, arrow, border, or page edge overlap occurs
- content is not too close to page edges
- the optional border does not crowd the content
- colors come from the SVG logo palette
- for `A3 on A4`, paired tiles reassemble into complete boards
- for `A3 on A4`, seam overlap prevents missing content
- for `A3 on A4`, trim/alignment marks are visible and usable

If any rendered page or reassembled board fails inspection, adjust the layout,
regenerate the PDF, render again, and repeat until the output is good enough
to hand over.

Do not describe a PDF as complete unless this verification has been performed.

## Printing Guidance for Delivered A3-on-A4 PDFs

When delivering an `A3 on A4` PDF, tell the user:

```text
Print at 100% / actual size. Do not use fit-to-page.
Use odd pages as left sheets and even pages as right sheets.
Trim the blank unprinted edge from the even/right page using the printed marks.
Place the cut edge over the matching marks on the odd/left page.
Glue or tape the overlap.
```

## Files

Tracked source/instruction files:

```text
AGENTS.md
README.md
generate_boards.py
logo.svg
skills/slaif-directional-boards/SKILL.md
skills/slaif-directional-boards/agents/openai.yaml
```

Generated local output:

```text
dist/
```

Local virtual environments and generated output should not be committed.

## Maintainer

Janez Perš  
Faculty of Electrical Engineering, University of Ljubljana  
Laboratory for Machine Intelligence (LMI)  
Email: janez.pers@fe.uni-lj.si

- Profile: https://lmi.fe.uni-lj.si/en/janez-pers-2/
- Laboratory: https://lmi.fe.uni-lj.si/en

## Security Contact

For responsible disclosure of vulnerabilities, please contact:  
janez.pers@fe.uni-lj.si

## Acknowledgement

We acknowledge the support of the EC/EuroHPC JU and the Slovenian Ministry of
HESI via the project SLAIF (grant number 101254461).

Project website: https://www.slaif.si
