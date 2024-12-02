from PIL import Image, ImageEnhance
import os

class saturateColor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.saturation_factor = 1.5

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            if self.image.format != "PNG":
                raise ValueError("Image is not in PNG format.")
        except IOError:
            print("Error: The file could not be opened.")
            return False
        return True

    def increase_saturation(self):
        if not self.load_image():
            return

        enhancer = ImageEnhance.Color(self.image)
        saturated_image = enhancer.enhance(self.saturation_factor)

        folder_name = "Saturated_Images"
        os.makedirs(folder_name, exist_ok=True)

        new_image_path = os.path.join(folder_name, os.path.splitext(os.path.basename(self.image_path))[0] + "_saturated.png")
        saturated_image.save(new_image_path)
        print(f"Saturated image saved at: {new_image_path}")

    def close_image(self):
        if self.image:
            self.image.close()
