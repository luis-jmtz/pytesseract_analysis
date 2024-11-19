from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
import math
from font_slanting import slant_glyph

# font loading, from https://freefontsfamily.org/times-new-roman-font-free/

font_path = f"golos-text_medium.ttf"
# using times new roman because it had a very high accuracy, and it isn't bold or itallized
font = TTFont(font_path)

modified_font_path = "modified_font.ttf"

# Boolean variable to enable/disable slanting
slant_mod = True

# Slant angle in degrees (positive for right slant, negative for left slant)
slant_angle = 15

if slant_mod:
    # Get the glyph set from the font
    glyph_set = font.getGlyphSet()

    # Iterate through all glyphs in the font
    for glyph_name in glyph_set.keys():
        glyph = glyph_set[glyph_name]  # Get the specific glyph
        try:
            # Apply slant transformation
            slant_glyph(glyph, slant_angle)
        except Exception as e:
            # Handle any exceptions for unsupported glyph types
            print(f"Could not modify glyph '{glyph_name}': {e}")

# Save the modified font
font.save(modified_font_path)
print(f"Modified font saved to {modified_font_path}")