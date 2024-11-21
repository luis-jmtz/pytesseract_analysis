import os
import svgwrite

def generate_A_svg(weight_value, slant_value, width_value, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Define the file name based on the naming convention
    file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"
    file_path = os.path.join(output_folder, file_name)

    # Function to create SVG for the capital letter A
    def create_character_svg(character, file_path):
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

        dwg = svgwrite.Drawing(filename=file_path, size=(f"{canvas_width}px", f"{canvas_height}px"))

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

    # Generate SVG for the capital letter A
    create_character_svg("A", file_path)

    return file_path

"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): Adjusts the proportions of text along X-axis. range: -50 -75

"""

# Specify the output folder
output_folder = "generated_svgs"

# Generate the SVG
temp = generate_A_svg(500, 0, 0, output_folder)
print(f"SVG file created: {temp}")
