import os
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph
from fontTools.ttLib.tables._c_m_a_p import table__c_m_a_p
from fontTools.ttLib.tables._h_e_a_d import table__h_e_a_d
from fontTools.ttLib.tables._h_m_t_x import table__h_m_t_x
from fontTools.ttLib.tables._m_a_x_p import table__m_a_x_p
from fontTools.pens.ttGlyphPen import TTGlyphPen


def create_font_from_svgs(svg_folder, output_font_name):
    """
    Create a TTF font from SVG files in the provided folder.

    :param svg_folder: Path to the folder containing the SVG files.
    :param output_font_name: Name of the output font file.
    """
    svg_folder = os.path.abspath(svg_folder)
    if not os.path.exists(svg_folder):
        raise FileNotFoundError(f"The folder '{svg_folder}' does not exist.")

    # Create a new font object
    font = TTFont()

    # Initialize necessary tables for the font
    font['head'] = table__h_e_a_d()
    font['hmtx'] = table__h_m_t_x()
    font['maxp'] = table__m_a_x_p()
    font['glyf'] = TTFont.newTable('glyf')  # Create an empty 'glyf' table
    font['cmap'] = table__c_m_a_p()
    font['cmap'].tableVersion = 0
    font['cmap'].tables = []

    # Glyph order and mappings
    glyph_order = ['.notdef']
    glyphs = {}
    cmap = {}

    # Iterate through SVG files in the folder
    for svg_file in sorted(os.listdir(svg_folder)):
        if svg_file.endswith('.svg'):
            char_name = os.path.splitext(svg_file)[0]
            unicode_val = get_unicode_from_name(char_name)

            # Parse SVG path data and create a glyph
            svg_path = os.path.join(svg_folder, svg_file)
            glyph = parse_svg_to_glyph(svg_path)

            # Add the glyph to the font
            glyph_name = f"glyph{unicode_val}"
            glyphs[glyph_name] = glyph
            glyph_order.append(glyph_name)
            cmap[unicode_val] = glyph_name

    # Assign glyphs and cmap to the font
    font.setGlyphOrder(glyph_order)
    font['glyf'].glyphs = glyphs
    cmap_table = table__c_m_a_p.CmapSubtable.newSubtable(4)  # Format 4 cmap
    cmap_table.platformID = 3  # Windows
    cmap_table.platEncID = 1   # Unicode
    cmap_table.language = 0
    cmap_table.cmap = cmap
    font['cmap'].tables.append(cmap_table)

    # Set basic font metadata
    font['maxp'].numGlyphs = len(glyph_order)

    # Save the font
    output_path = os.path.join(svg_folder, output_font_name)
    font.save(output_path)
    print(f"Font saved at: {output_path}")


def get_unicode_from_name(name):
    """
    Map a file name to a Unicode character based on naming conventions.

    :param name: Name of the SVG file (e.g., 'a_lower', 'A_upper', '8').
    :return: Unicode code point for the character.
    """
    if name.isdigit():
        return ord(name)  # Return Unicode for numbers
    elif name.endswith("_lower"):
        return ord(name[0])  # Lowercase letters
    elif name.endswith("_upper"):
        return ord(name[0].upper())  # Uppercase letters
    else:
        raise ValueError(f"Invalid character name: {name}")


def parse_svg_to_glyph(svg_path):
    """
    Parse an SVG file and convert it into a Glyph object.

    :param svg_path: Path to the SVG file.
    :return: Glyph object.
    """
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Extract the 'd' attribute from the <path> element
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    path_element = root.find('.//svg:path', namespace)
    if path_element is None or 'd' not in path_element.attrib:
        raise ValueError(f"No valid <path> element found in {svg_path}")

    path_data = path_element.attrib['d']

    # Create a Glyph using TTGlyphPen
    pen = TTGlyphPen(None)
    # Here, implement logic to parse 'd' path_data into the pen
    # This example assumes you provide logic to interpret path_data
    pen.moveTo((0, 0))  # Placeholder
    pen.lineTo((100, 100))  # Placeholder
    pen.closePath()

    return pen.glyph()


if __name__ == "__main__":
    # Example usage
    folder_name = "weight500_slant0_width0"
    output_font = "custom_font.ttf"
    create_font_from_svgs(folder_name, output_font)
