# import os
# from cairosvg import svg2png


# class SVGToPNG:
#     def __init__(self, input_folder, output_folder):

#         self.input_folder = input_folder
#         self.output_folder = output_folder

#         # Ensure the output folder exists
#         os.makedirs(self.output_folder, exist_ok=True)

#     def convert_all(self):

#         # Get a list of all SVG files in the input folder
#         svg_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.svg')]

#         # Convert each SVG file to PNG
#         for svg_file in svg_files:
#             input_path = os.path.join(self.input_folder, svg_file)
#             output_file = os.path.splitext(svg_file)[0] + '.png'  # Replace .svg with .png
#             output_path = os.path.join(self.output_folder, output_file)

#             # Read SVG and add white background
#             with open(input_path, 'rb') as svg_input:
#                 svg_data = svg_input.read()
#                 # Convert SVG to PNG with a white background
#                 svg2png(bytestring=svg_data, write_to=output_path, output_width=None, background_color="white")

#             print(f"Converted: {svg_file} -> {output_file}")

#         print(f"All SVG files have been converted and saved to: {self.output_folder}")

import os
from cairosvg import svg2png
import xml.etree.ElementTree as ET


class SVGToPNG:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def _get_svg_dimensions(self, svg_path):
        """
        Extract width and height from the SVG file to determine scaling.
        """
        try:
            tree = ET.parse(svg_path)
            root = tree.getroot()

            width = root.attrib.get("width")
            height = root.attrib.get("height")

            # Convert dimensions to floats, handling units like 'px'
            if width and height:
                width = float(width.replace("px", ""))
                height = float(height.replace("px", ""))
                return width, height
            else:
                # Return None if dimensions are missing
                return None, None
        except Exception as e:
            print(f"Error reading dimensions for {svg_path}: {e}")
            return None, None

    def convert_all(self):
        """
        Convert all SVG files in the input folder to PNGs,
        scaling them to ensure a minimum width/height of 500px.
        """
        # Get a list of all SVG files in the input folder
        svg_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.svg')]

        # Convert each SVG file to PNG
        for svg_file in svg_files:
            input_path = os.path.join(self.input_folder, svg_file)
            output_file = os.path.splitext(svg_file)[0] + '.png'  # Replace .svg with .png
            output_path = os.path.join(self.output_folder, output_file)

            # Get original dimensions
            width, height = self._get_svg_dimensions(input_path)

            # Determine scaling factor to achieve a minimum of 500px
            scale_factor = 1  # Default scale factor
            if width and height:
                scale_factor = max(500 / width, 500 / height)

            # Read SVG and convert to PNG
            with open(input_path, 'rb') as svg_input:
                svg_data = svg_input.read()

                # Apply scaling while converting SVG to PNG
                svg2png(
                    bytestring=svg_data,
                    write_to=output_path,
                    scale=scale_factor,
                    background_color="white"
                )

            print(f"Converted: {svg_file} -> {output_file}")

        print(f"All SVG files have been converted and saved to: {self.output_folder}")
