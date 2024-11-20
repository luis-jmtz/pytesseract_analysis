import os
import svgwrite


def generate_alphanumeric_svgs(weight_value, slant_value, width_value, curviness_value):
    # Define alphanumeric characters
    numbers = [chr(i) for i in range(48, 58)]  # Digits 0-9
    uppercase = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
    lowercase = [chr(i) for i in range(97, 123)]  # Lowercase a-z

    # Combine all characters
    alphanumeric_chars = numbers + uppercase + lowercase

    # Define output folder naming convention
    folder_name = f"weight{weight_value}_slant{slant_value}_width{width_value}_curviness{curviness_value}"
    output_folder = os.path.join(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Function to create basic geometric shapes for characters
    def create_character_svg(character, folder):
        filename = f"{character}.svg"
        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=("100px", "100px"))
        center_x, center_y = 50, 50  # Center of the SVG canvas

        stroke_width = weight_value / 100
        char_width = 20 + width_value
        char_height = 40 + curviness_value
        slant_offset = slant_value / 2

        if character.isdigit():
            # Create shapes for digits
            if character == '0':
                dwg.add(dwg.ellipse(center=(center_x, center_y), r=(char_width / 2, char_height / 2),
                                    stroke="black", fill="none", stroke_width=stroke_width))
            elif character == '1':
                dwg.add(dwg.line(start=(center_x, center_y - char_height / 2),
                                 end=(center_x, center_y + char_height / 2),
                                 stroke="black", stroke_width=stroke_width))
            elif character == '2':
                dwg.add(dwg.polyline(points=[
                    (center_x - char_width / 2, center_y - char_height / 2),
                    (center_x + char_width / 2, center_y - char_height / 2),
                    (center_x - char_width / 2, center_y + char_height / 2),
                    (center_x + char_width / 2, center_y + char_height / 2)
                ], stroke="black", fill="none", stroke_width=stroke_width))
            # Add shapes for other digits...

        elif character.isupper():
            # Create shapes for uppercase letters
            if character == 'A':
                dwg.add(dwg.polygon(points=[
                    (center_x, center_y - char_height / 2),
                    (center_x - char_width / 2, center_y + char_height / 2),
                    (center_x + char_width / 2, center_y + char_height / 2)
                ], fill="none", stroke="black", stroke_width=stroke_width))
                dwg.add(dwg.line(start=(center_x - char_width / 4, center_y),
                                 end=(center_x + char_width / 4, center_y),
                                 stroke="black", stroke_width=stroke_width))
            elif character == 'B':
                dwg.add(dwg.line(start=(center_x - char_width / 2, center_y - char_height / 2),
                                 end=(center_x - char_width / 2, center_y + char_height / 2),
                                 stroke="black", stroke_width=stroke_width))
                dwg.add(dwg.ellipse(center=(center_x, center_y - char_height / 4), r=(char_width / 3, char_height / 4),
                                    stroke="black", fill="none", stroke_width=stroke_width))
                dwg.add(dwg.ellipse(center=(center_x, center_y + char_height / 4), r=(char_width / 3, char_height / 4),
                                    stroke="black", fill="none", stroke_width=stroke_width))
            # Add shapes for other uppercase letters...

        elif character.islower():
            # Create shapes for lowercase letters
            if character == 'a':
                dwg.add(dwg.circle(center=(center_x, center_y), r=char_width / 2, stroke="black",
                                   fill="none", stroke_width=stroke_width))
                dwg.add(dwg.line(start=(center_x + char_width / 2, center_y),
                                 end=(center_x + char_width / 2, center_y + char_height / 2),
                                 stroke="black", stroke_width=stroke_width))
            elif character == 'b':
                dwg.add(dwg.line(start=(center_x - char_width / 2, center_y - char_height / 2),
                                 end=(center_x - char_width / 2, center_y + char_height / 2),
                                 stroke="black", stroke_width=stroke_width))
                dwg.add(dwg.ellipse(center=(center_x, center_y), r=(char_width / 3, char_height / 3),
                                    stroke="black", fill="none", stroke_width=stroke_width))
            # Add shapes for other lowercase letters...

        dwg.save()

    # Generate SVGs for all alphanumeric characters
    for char in alphanumeric_chars:
        create_character_svg(char, output_folder)

    """
    Parameters:
        weight_value (int): Line thickness.
        slant_value (int): Font slant in degrees (-ve for backward, +ve for forward).
        width_value (float): Adjusts the proportions of counters, strokes, spacing, and kerning.
        curviness_value (int): Level of curviness (0 is angular, higher values are more curved).
    """

# Generate SVGs with specified parameters
generate_alphanumeric_svgs(600, 0, 10, 0)
