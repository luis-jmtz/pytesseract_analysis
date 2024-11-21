import os
import svgwrite

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

        # Calculate scaling factor for X-axis based on width_value
        scale_x = 1 + (width_value / 100)  # Positive stretches, negative squeezes
        scale_y = 1  # Keep Y-axis scaling fixed

        # Adjust canvas size dynamically based on scaling
        base_canvas_width = 100  # Base canvas size
        canvas_width = int(base_canvas_width * scale_x)  # Dynamically scale width
        canvas_height = 100  # Fixed height

        # Center character dynamically
        insert_x = canvas_width / 2
        insert_y = "50%"  # Center character vertically

        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=(f"{canvas_width}px", f"{canvas_height}px"))

        # Apply text transformations and styling based on parameters
        font_style = f"skewX({-slant_value})"  # Apply slant transformation

        # Use `font-weight` up to 900, and simulate additional weight with stroke
        effective_weight = min(weight_value, 900)  # Limit font-weight to max 900
        stroke_weight = max(0, (weight_value - 900) * 0.005)  # Gradual increase in stroke thickness

        # Combine scaling and slant transformations
        transform = f"{font_style} scale({scale_x}, {scale_y})"

        dwg.add(dwg.text(
            character,
            insert=(f"{insert_x}px", insert_y),
            text_anchor="middle",
            alignment_baseline="middle",
            font_size="18px",  # Fixed font size
            font_weight=str(effective_weight),  # Adjust thickness
            font_family="Arial",  # Simplified styling, can be extended for variety
            fill="black",
            stroke="black",  # Add stroke to simulate extra weight
            stroke_width=f"{stroke_weight}px",  # Adjust stroke width for additional weight
            transform=transform  # Apply combined transformations
        ))
        dwg.save()

    # Generate SVGs for all alphanumeric characters
    for char in alphanumeric_chars:
        create_character_svg(char, output_folder)


"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): Adjusts the proportions of text along X-axis.
                         - Negative values squeeze the text.
                         - Positive values stretch the text.
                         - A value of 100 doubles the width.
"""

# Generate SVGs with specified parameters
generate_alphanumeric_svgs(500, 0, 75)  # Example: Stretch along X-axis by 100%
