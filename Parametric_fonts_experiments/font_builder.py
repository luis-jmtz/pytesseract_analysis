from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
import math

# font loading, from https://freefontsfamily.org/times-new-roman-font-free/

font_path = f"times new roman.ttf"
# using times new roman because it had a very high accuracy, and it isn't bold or itallized
font = TTFont(font_path)

def slant_glyph(glyph, angle_deg):
    angle_rad = math.radians(angle_deg)
    slant_matrix = (1, 0, math.tan(angle_rad), 1, 0, 0)
    pen = TransformPen(glyph, slant_matrix)
    glyph.draw(pen)

# Save the modified font
font.save("modified_font.ttf")