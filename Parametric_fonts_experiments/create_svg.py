import svgwrite

def generate_A_svg(weight_value, slant_value, width_value):
    # Define the file name based on the previous folder naming convention
    file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"

    # Function to create SVG for the capital letter A
    def create_character_svg(character, file_name):
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

        dwg = svgwrite.Drawing(filename=file_name, size=(f"{canvas_width}px", f"{canvas_height}px"))

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
    create_character_svg("A", file_name)

    return file_name

"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): Adjusts the proportions of text along X-axis. range: -50 -75

"""

temp = generate_A_svg(1200, 0, 0)
print(f"SVG file created: {temp}")
