import os
from PIL import Image

class staggeredWhiteSpacer:
    def __init__(self, image_path, output_folder):
        self.image_path = image_path
        self.output_folder = output_folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def add_staggered_white_lines(self, num_lines, position=0):

        #0 - Adds white space evenly at the top and bottom.
        #1 - Adds more white space at the top and one less at the bottom.
        #2 - Adds more white space at the bottom and one less at the top.

        try:
            img = Image.open(self.image_path)
            width, height = img.size

            if position == 1:  # More white space at the top, one less at the bottom
                top_space = num_lines
                bottom_space = num_lines - 1
            elif position == 2:  # More white space at the bottom, one less at the top
                top_space = num_lines - 1
                bottom_space = num_lines
            else:  # Default: Even white space at the top and bottom
                top_space = bottom_space = num_lines

            new_height = height + top_space + bottom_space
            new_img = Image.new("RGB", (width, new_height), "white")
            new_img.paste(img, (0, top_space))

            output_path = os.path.join(self.output_folder, f"{num_lines}_staggeredWhiteSpace_position{position}.png")
            new_img.save(output_path)
            return output_path
        except Exception as e:
            return str(e)
