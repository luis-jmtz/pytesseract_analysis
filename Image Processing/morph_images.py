import cv2
import numpy as np
from PIL import Image
import os

class morph_processor:
    def __init__(self, image_path, base_name):
        self.image_path = image_path
        self.base_name = base_name
        self.image = None
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # Kernel size 3x3

    def load_image(self):
        try:
            # Open the image in grayscale mode for processing
            self.image = Image.open(self.image_path).convert("L")
        except IOError:
            print("Error: Unable to open the file.")
            return False
        return True

    def apply_morphology(self):
        if not self.load_image():
            return

        # Convert the Pillow image to a NumPy array for OpenCV processing
        image_np = np.array(self.image)

        # Apply morphological opening
        opened_image = cv2.morphologyEx(image_np, cv2.MORPH_OPEN, self.kernel)

        # Apply morphological closing
        closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, self.kernel)

        # Convert the final processed image back to a Pillow image
        morphed_image = Image.fromarray(closed_image)

        # Save the processed image
        morphed_image_path = f"{self.base_name}_morphed.png"
        morphed_image.save(morphed_image_path)
        print(f"Morphs complete. Image saved at: {morphed_image_path}")

    def close_image(self):
        if self.image:
            self.image.close()
