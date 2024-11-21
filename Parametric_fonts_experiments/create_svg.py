# import os
# import svgwrite
# import math


# class SVGGenerator:
#     def __init__(self):
#         # Hardcoded output folder
#         self.output_folder = "generated_svgs"
#         # Ensure the output folder exists
#         os.makedirs(self.output_folder, exist_ok=True)

#     def generate(self, weight_value, slant_value, width_value):

#         # Define the file name based on the naming convention
#         file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"
#         file_path = os.path.join(self.output_folder, file_name)

#         # Generate SVG for the capital letter A
#         self._create_character_svg("A", weight_value, slant_value, width_value, file_path)

#         return file_path

#     def _create_character_svg(self, character, weight_value, slant_value, width_value, file_path):
#         # Base font size to calculate dimensions
#         font_size = 30

#         # Scaling factors based on width_value
#         scale_x = 1 + (width_value / 100)  # Positive stretches, negative squeezes
#         scale_y = 1

#         # Calculate approximate text dimensions
#         text_width = font_size * 0.6 * scale_x  # Adjust width by scale_x
#         text_height = font_size * scale_y  # Adjust height by scale_y

#         # Adjust for slant transformation (calculate extra width required on the left)
#         slant_radians = math.radians(slant_value)
#         left_padding_adjustment = text_height * abs(math.tan(slant_radians))

#         # Add generous padding to account for slant, width scaling, and extra margin
#         padding = 0.4 * max(text_width, text_height)  # Increase padding to 30% of largest dimension
#         canvas_width = text_width + left_padding_adjustment + 2.5 * padding  # Extra horizontal padding
#         canvas_height = text_height + 2 * padding  # Vertical padding

#         # Calculate the text insertion point (adjust for left-side slant padding)
#         insert_x = left_padding_adjustment + (canvas_width - left_padding_adjustment) / 2
#         insert_y = canvas_height / 2

#         # Create the SVG canvas
#         dwg = svgwrite.Drawing(
#             filename=file_path,
#             size=(f"{canvas_width}px", f"{canvas_height}px")
#         )

#         # Apply text transformations
#         font_style = f"skewX({-slant_value})"  # Apply slant transformation
#         transform = f"{font_style} scale({scale_x}, {scale_y})"

#         # Calculate effective weight and stroke
#         effective_weight = min(weight_value, 900)
#         stroke_weight = max(0, (weight_value - 900) * 0.005)

#         # Add the character text to the SVG
#         dwg.add(dwg.text(
#             character,
#             insert=(f"{insert_x}px", f"{insert_y}px"),
#             text_anchor="middle",
#             alignment_baseline="middle",
#             font_size=f"{font_size}px",
#             font_weight=str(effective_weight),
#             font_family="Arial",
#             fill="black",
#             stroke="black",
#             stroke_width=f"{stroke_weight}px",
#             transform=transform
#         ))

#         # Save the SVG
#         dwg.save()
import os


class SVGGenerator:
    def __init__(self, output_folder="generated_svgs", font_size=30, padding_scale=.8, extra_right_padding_scale=2):
        self.output_folder = output_folder
        self.font_size = font_size  # Base font size
        self.padding_scale = padding_scale  # Padding scale relative to font size
        self.extra_right_padding_scale = extra_right_padding_scale  # Additional right padding scale

        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate(self, weight_value=400, slant_value=0, width_value=0, text="AB ab"):

        # Adjust font width based on `width_value`
        adjusted_width_factor = max(0.5, 1 + width_value / 100)  # Ensure width factor is not negative
        adjusted_font_size = self.font_size * adjusted_width_factor

        # Adjust slant effect
        slant_offset = abs(slant_value) / 60  # Calculate slant effect (max 60 degrees)
        slant_padding = self.font_size * slant_offset

        # Dynamically determine canvas size and padding
        dynamic_padding = self.font_size * self.padding_scale  # Base padding relative to font size
        extra_right_padding = self.font_size * self.extra_right_padding_scale  # Extra padding for the right
        text_length = len(text)

        # Calculate width with slant and width effects
        width = text_length * adjusted_font_size // 2 + 2 * dynamic_padding + extra_right_padding + slant_padding

        # Calculate height with slant effects
        height = self.font_size + 2 * dynamic_padding + slant_padding

        # Generate file name based on parameters
        file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"

        # Start SVG content
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}px" height="{height}px" viewBox="0 0 {width} {height}">
            <rect width="100%" height="100%" fill="white"/>
        """

        # Add text element to SVG
        x_position = dynamic_padding
        y_position = dynamic_padding + self.font_size

        svg_content += f"""<text x="{x_position}" y="{y_position}" font-family="Arial" 
            font-size="{adjusted_font_size}" font-weight="{weight_value}" 
            transform="skewX({slant_value})" fill="black">{text}</text>"""

        # Close SVG content
        svg_content += "</svg>"

        # Write SVG to file
        output_path = os.path.join(self.output_folder, file_name)
        with open(output_path, "w") as svg_file:
            svg_file.write(svg_content)

        print(f"SVG created: {output_path}")
        return output_path




