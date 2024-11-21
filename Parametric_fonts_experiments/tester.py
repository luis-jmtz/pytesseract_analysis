import os
import svgwrite
from xml.etree import ElementTree as ET

def generate_alphanumeric_svgs(weight_value, slant_value, width_value):
    # Define alphanumeric characters
    numbers = [chr(i) for i in range(48, 58)]  # Digits 0-9
    uppercase = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
    lowercase = [chr(i) for i in range(97, 123)]  # Lowercase a-z

    # Combine all characters
    alphanumeric_chars = numbers + uppercase + lowercase

    # Define output folder naming convention
    folder_name = f"weight{weight_value}_slant{slant_value}_width{width_value}"
    output_folder = os.path.join(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Function to create SVGs for alphanumeric characters
    def create_character_svg(character, folder):
        if character.isupper():
            filename = f"{character}_upper.svg"
        elif character.islower():
            filename = f"{character}_lower.svg"
        else:  # Digits
            filename = f"{character}.svg"

        # Adjust canvas size and offsets dynamically
        slant_padding = abs(slant_value) * 2
        canvas_width = 100 + slant_padding  # Increase canvas width to accommodate slant
        canvas_height = 100
        insert_x = canvas_width / 2  # Center character horizontally
        insert_y = "50%"  # Center character vertically

        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=(f"{canvas_width}px", f"{canvas_height}px"))

        # Calculate scaling for width adjustment
        scale_x = 1 + width_value  # Stretch/squeeze x-axis; width_value=0 is default
        scale_x = max(0.1, scale_x)  # Prevent scale from collapsing completely (set a lower limit)

        # Apply text transformations and styling based on parameters
        font_style = f"skewX({-slant_value})"  # Apply slant transformation

        dwg.add(dwg.text(
            character,
            insert=(f"{insert_x}px", insert_y),
            text_anchor="middle",
            alignment_baseline="middle",
            font_size="18px",  # Fixed font size
            font_weight=str(weight_value),  # Adjust thickness
            font_family="Arial",  # Simplified styling, can be extended for variety
            fill="black",
            transform=f"{font_style} scale({scale_x}, 1)",  # Scale x-axis only
        ))
        dwg.save()

        # Optimize the canvas size after saving
        optimize_canvas(os.path.join(folder, filename))

    # Generate SVGs for all alphanumeric characters
    for char in alphanumeric_chars:
        create_character_svg(char, output_folder)


def optimize_canvas(svg_file):
    """Optimize the SVG canvas size to fit the content."""
    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Define the SVG namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', ns['svg'])

    # Find the bounding box of all elements
    elements = root.findall(".//svg:*", ns)
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')

    for elem in elements:
        if 'x' in elem.attrib and 'y' in elem.attrib and 'width' in elem.attrib and 'height' in elem.attrib:
            x = float(elem.attrib.get('x', 0))
            y = float(elem.attrib.get('y', 0))
            width = float(elem.attrib.get('width', 0))
            height = float(elem.attrib.get('height', 0))

            # Update bounds
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x + width)
            max_y = max(max_y, y + height)

    # Calculate new viewBox and dimensions
    if min_x < float('inf') and min_y < float('inf'):
        new_width = max_x - min_x
        new_height = max_y - min_y
        viewBox = f"{min_x} {min_y} {new_width} {new_height}"

        # Update the root element
        root.attrib['viewBox'] = viewBox
        root.attrib['width'] = str(new_width)
        root.attrib['height'] = str(new_height)

        # Write the changes back to the SVG file
        tree.write(svg_file)


"""
Parameters:
    weight_value (int): Line thickness.
    slant_value (int): Font slant in degrees (-ve for backward, +ve for forward).
    width_value (float): Stretch/squeeze factor for x-axis (0 = default, negative = squeeze, positive = stretch).
"""

# Generate SVGs with specified parameters
generate_alphanumeric_svgs(1200, 60, 0.5)  # Example: Slightly stretch the width
