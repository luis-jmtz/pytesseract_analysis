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
            png_path = os.path.splitext(self.image_path)[0] + ".png"
            folder_name = "PNG_Images"
            os.makedirs(folder_name, exist_ok=True)
            png_path = os.path.join(folder_name, os.path.basename(png_path))
            self.image.save(png_path, "PNG")
            print(f"PNG image saved at: {png_path}")
        else:
            print("The image is not in JPEG format; no conversion needed.")

    def close_image(self):
        if self.image:
            self.image.close()
