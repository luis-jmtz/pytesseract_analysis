import math
from fontTools.pens.transformPen import TransformPen

#from chatGPT

def slant_glyph(glyph, angle_deg):
    """
    Applies a slant transformation to a glyph outline, modifying its appearance by skewing it.

    Parameters:
    glyph: A Glyph object from the font that contains the path of the character shape.
           It has methods to draw its outline and modify its contours.
    angle_deg: The angle in degrees by which the glyph will be slanted. Positive angles
               slant to the right, negative angles slant to the left.

    Returns:
    None: The function modifies the glyph in-place.
    """
    # Step 1: Convert the angle from degrees to radians
    # Since mathematical functions use radians, we need to convert degrees to radians.
    angle_rad = math.radians(angle_deg)

    # Step 2: Define the transformation matrix for slanting
    # The slanting matrix is of the form:
    #   [1, tan(angle), 0]
    #   [0,      1,     0]
    # This matrix skews the glyph horizontally while preserving its vertical proportions.
    slant_matrix = (1, 0, math.tan(angle_rad), 1, 0, 0)

    # Step 3: Create a TransformPen for applying the slant
    # The TransformPen wraps the glyph and applies the transformation matrix to its outline.
    pen = TransformPen(glyph.getPen(), slant_matrix)

    # Step 4: Redraw the glyph with the transformation applied
    # The glyph's draw() method recreates its outline, sending its contours through the TransformPen.
    glyph.draw(pen)

    # Note: TransformPen modifies the glyph's internal representation directly,
    # so there is no need to return anything.
