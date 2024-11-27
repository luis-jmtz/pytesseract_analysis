from PIL import Image
import os

class toPNG:
    def __init__(self, image_path):

        self.image_path = image_path
        self.image = None

    def load_image(self):

        try:
            self.image = Image.open(self.image_path)
        except IOError:
            print("Error: The file could not be opened.")
            return False
        return True

    def is_jpeg(self):

        return self.image.format.lower() in ['jpeg', 'jpg']

    def convert_to_png(self):

        if not self.load_image():
            return

        if self.is_jpeg():
            # Set the new file name
            png_path = os.path.splitext(self.image_path)[0] + ".png"
            self.image.save(png_path, "PNG")
        else:
            print("The image is not in JPEG format; no conversion needed.")
    
    def close_image(self):

        if self.image:
            self.image.close()
