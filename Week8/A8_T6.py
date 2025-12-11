from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing) -> None:
    # ...
    PDwg.add(Rect(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#rect
    return None

def drawCircle(PDwg: Drawing) -> None:
    # ...
    PDwg.add(Circle(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#circle
    return None

def saveSvg(PDwg: Drawing) -> None:
    # See Drawing.save method https://svgwrite.readthedocs.io/en/latest/classes/drawing.html?highlight=save#svgwrite.drawing.Drawing.save
    return None

def main() -> None:
    # 1. Initialise
    Dwg = svgwrite.Drawing()
    # ...
        drawSquare(Dwg)
        drawCircle(Dwg)
    # 3. Cleanup
    return None