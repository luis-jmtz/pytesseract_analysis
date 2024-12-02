from PIL import Image

class whiteSpacer:
    def __init__(self, image_path):
        self.image_path = image_path

    def add_white_lines(self, num_lines, position=0):


        #0 - Adds white space evenly at the top and bottom.
        #1 - Adds white space only at the top.
        #2 - Adds white space only at the bottom.

        try:
            img = Image.open(self.image_path)
            width, height = img.size

            if position == 1:  # Add white space only at the top
                new_height = height + num_lines
                new_img = Image.new("RGB", (width, new_height), "white")
                new_img.paste(img, (0, num_lines))
            elif position == 2:  # Add white space only at the bottom
                new_height = height + num_lines
                new_img = Image.new("RGB", (width, new_height), "white")
                new_img.paste(img, (0, 0))
            else:  # Default: Add white space evenly at top and bottom
                new_height = height + (2 * num_lines)
                new_img = Image.new("RGB", (width, new_height), "white")
                new_img.paste(img, (0, num_lines))

            output_path = fr"B_white_space_images\{num_lines}_whiteSpace.png"
            new_img.save(output_path)
            return output_path
        except Exception as e:
            return str(e)
