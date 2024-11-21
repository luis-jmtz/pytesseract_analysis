from PIL import Image, ImageEnhance
import os

class saturateColor:
    def __init__(self, image_path):

        self.image_path = image_path
        self.image = None
        self.saturation_factor = 1.5  # Hard-coded saturation increase factor

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

        # Enhance the saturation using the hard-coded saturation factor
        enhancer = ImageEnhance.Color(self.image)
        saturated_image = enhancer.enhance(self.saturation_factor)
        
        # Save the enhanced image
        new_image_path = os.path.splitext(self.image_path)[0] + "_saturated.png"
        saturated_image.save(new_image_path)
        print(f"Saturated image saved at: {new_image_path}")
    
    def close_image(self):

        if self.image:
            self.image.close()