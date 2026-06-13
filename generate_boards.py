from pathlib import Path
from reportlab.graphics import renderPDF
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg


TITLE = "Delavnica Orkestrirano agentno programiranje"
OUTPUT = Path("dist/slaif-directional-boards-a3-on-a4-overlap.pdf")
LOGO = Path("logo.svg")
BORDER = True
TOTAL_OVERLAP_MM = 25
TRIM_GUIDE_MM = 10
POINTS_PER_MM = 72 / 25.4

GREEN = HexColor("#87a73e")
GRAY = HexColor("#919395")

DIRECTIONS = [
    ("Up", 0),
    ("Right", -90),
    ("Left", 90),
    ("Down", 180),
    ("Up-right", -45),
    ("Down-right", -135),
    ("Down-left", 135),
    ("Up-left", 45),
]


def fit_lines(text, font_name, font_size, max_width):
    words = text.split()
    lines = []
    current = []

    for word in words:
        candidate = " ".join(current + [word])
        if pdfmetrics.stringWidth(candidate, font_name, font_size) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]

    if current:
        lines.append(" ".join(current))

    return lines


def draw_logo(c, drawing, x, y, width):
    scale = width / drawing.width
    height = drawing.height * scale
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    renderPDF.draw(drawing, c, 0, 0)
    c.restoreState()
    return height


def draw_arrow(c, x, y, rotation, scale=1):
    c.saveState()
    c.translate(x, y)
    c.rotate(rotation)
    c.scale(scale, scale)
    c.setFillColor(GREEN)
    c.setStrokeColor(GREEN)
    c.setLineJoin(1)

    points = [
        (-28, -108),
        (28, -108),
        (28, 46),
        (92, 46),
        (0, 132),
        (-92, 46),
        (-28, 46),
    ]
    path = c.beginPath()
    path.moveTo(*points[0])
    for point in points[1:]:
        path.lineTo(*point)
    path.close()
    c.drawPath(path, stroke=0, fill=1)
    c.restoreState()


def draw_board(c, drawing, direction, rotation, page_width, page_height):
    c.setFillColor(white)
    c.rect(0, 0, page_width, page_height, stroke=0, fill=1)

    if BORDER:
        margin = 32
        c.setStrokeColor(GRAY)
        c.setLineWidth(2)
        c.roundRect(
            margin,
            margin,
            page_width - 2 * margin,
            page_height - 2 * margin,
            18,
            stroke=1,
            fill=0,
        )

    logo_width = 450
    logo_x = 110
    logo_y = 165
    draw_logo(c, drawing, logo_x, logo_y, logo_width)

    font_name = "DejaVuSans-Bold"
    font_size = 64
    title_width = 1010
    lines = fit_lines(TITLE, font_name, font_size, title_width)
    leading = 78
    title_x = (page_width - title_width) / 2
    title_top = 710

    c.setFillColor(GREEN)
    c.setFont(font_name, font_size)
    for index, line in enumerate(lines):
        line_width = pdfmetrics.stringWidth(line, font_name, font_size)
        c.drawString(title_x + (title_width - line_width) / 2, title_top - index * leading, line)

    draw_arrow(c, page_width * 0.74, 290, rotation, scale=1.55)


def draw_seam_marks(c, tile_index, tile_width, tile_height):
    total_overlap = TOTAL_OVERLAP_MM * POINTS_PER_MM
    trim_guide = TRIM_GUIDE_MM * POINTS_PER_MM
    usable_overlap = total_overlap - trim_guide

    if tile_index == 0:
        mark_x = tile_width - usable_overlap
    else:
        mark_x = trim_guide

    c.saveState()
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.8)
    c.setDash(4, 4)

    top_y1 = tile_height - 74
    top_y2 = tile_height - 24
    bottom_y1 = 24
    bottom_y2 = 74
    tick = 12

    c.line(mark_x, bottom_y1, mark_x, bottom_y2)
    c.line(mark_x, top_y1, mark_x, top_y2)

    c.setDash()
    c.line(mark_x - tick, bottom_y2, mark_x + tick, bottom_y2)
    c.line(mark_x - tick, top_y1, mark_x + tick, top_y1)
    c.restoreState()


def draw_tiled_page(c, drawing, direction, rotation, tile_index):
    tile_width, tile_height = portrait(A4)
    overlap = TOTAL_OVERLAP_MM * POINTS_PER_MM
    board_width = 2 * tile_width - overlap
    board_height = tile_height
    source_x = tile_index * (tile_width - overlap)

    c.saveState()
    clip = c.beginPath()
    clip.rect(0, 0, tile_width, tile_height)
    c.clipPath(clip, stroke=0, fill=0)
    c.translate(-source_x, 0)
    draw_board(c, drawing, direction, rotation, board_width, board_height)
    c.restoreState()
    draw_seam_marks(c, tile_index, tile_width, tile_height)
    c.showPage()


def main():
    if not LOGO.exists():
        raise SystemExit("Missing required logo.svg")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(font_path)))

    drawing = svg2rlg(str(LOGO))
    c = canvas.Canvas(str(OUTPUT), pagesize=portrait(A4))
    c.setTitle("SLAIF Directional Boards A3 on A4 with Overlap")
    c.setAuthor("SLAIF")

    for direction, rotation in DIRECTIONS:
        draw_tiled_page(c, drawing, direction, rotation, tile_index=0)
        draw_tiled_page(c, drawing, direction, rotation, tile_index=1)

    c.save()


if __name__ == "__main__":
    main()
