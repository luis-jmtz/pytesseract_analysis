from PIL import Image

class whiteSpacer:
    def __init__(self, image_path):
        self.image_path = image_path

    def add_white_lines(self, num_lines):
        try:
            img = Image.open(self.image_path)
            width, height = img.size
            new_height = height + (2 * num_lines)
            new_width = width
            new_img = Image.new("RGB", (new_width, new_height), "white")
            new_img.paste(img, (0, num_lines))
            output_path = fr"white_space_images\{num_lines}_whiteSpace.png"
            new_img.save(output_path)
            return output_path
        except Exception as e:
            return str(e)
