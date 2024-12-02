from PIL import Image
import os

class upscaleImage:
    def __init__(self, image_path, base_name):
        self.image_path = image_path
        self.image = None
        self.scale_factor = 1.5
        self.base_name = base_name

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
        except IOError:
            print("Error: The file could not be opened.")
            return False
        return True

    def upscale_image(self):
        if not self.load_image():
            return

        new_width = int(self.image.width * self.scale_factor)
        new_height = int(self.image.height * self.scale_factor)

        upscaled_image = self.image.resize((new_width, new_height), Image.LANCZOS)

        folder_name = "Upscaled_Images"
        os.makedirs(folder_name, exist_ok=True)

        new_image_path = os.path.join(folder_name, f"{self.base_name}_upscaled.png")
        upscaled_image.save(new_image_path)
        print(f"Upscaled image saved at: {new_image_path}")

    def close_image(self):
        if self.image:
            self.image.close()
