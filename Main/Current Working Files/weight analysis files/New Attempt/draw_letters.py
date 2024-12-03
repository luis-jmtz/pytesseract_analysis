import os
from PIL import Image, ImageDraw

class LetterDrawer:
    def __init__(self, line_thickness, output_folder):
        self.line_thickness = line_thickness
        self.output_folder = output_folder
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def draw_and_save(self):
        # Image dimensions
        image_width, image_height = 500, 500

        # Create a blank image with white background
        image = Image.new('RGB', (image_width, image_height), 'white')
        draw = ImageDraw.Draw(image)

        # Dimensions and spacing of the "A"
        a_height = 20  # Height of each "A"
        base_spacing = 12  # Space between the bases of the "A"s
        a_width = a_height // 2  # Proportional width of "A"
        half_width = a_width // 2

        # Calculate horizontal positions for the "A"s
        total_width = 4 * a_width + 3 * base_spacing
        start_x = (image_width - total_width) // 2
        y_top = (image_height - a_height) // 2

        for i in range(4):
            # Base X position of the current "A"
            base_x = start_x + i * (a_width + base_spacing)

            # Points for the "A"
            left_leg = (base_x, y_top + a_height)
            right_leg = (base_x + a_width, y_top + a_height)
            top = (base_x + half_width, y_top)
            crossbar_left = (base_x + a_width // 4, y_top + a_height // 2)
            crossbar_right = (base_x + 3 * a_width // 4, y_top + a_height // 2)

            # Draw the "A"
            draw.line([left_leg, top], fill='black', width=int(self.line_thickness))
            draw.line([right_leg, top], fill='black', width=int(self.line_thickness))
            draw.line([crossbar_left, crossbar_right], fill='black', width=int(self.line_thickness))

        # Construct file name and save the image
        file_name = f"{self.line_thickness}_thickness.png"
        file_path = os.path.join(self.output_folder, file_name)
        image.save(file_path)
        print(f"Image saved as '{file_path}'")