from PIL import Image
import cv2
import numpy as np
import os

class imageBnW:
    def __init__(self, image_path, base_name):
        self.image_path = image_path
        self.base_name = base_name
        self.image = None

    def load_image(self):
        try:
            self.image = Image.open(self.image_path).convert("L")
        except IOError:
            print("Error: The file could not be opened.")
            return False
        return True

    def convert_to_bnw(self):
        if not self.load_image():
            return

        image_np = np.array(self.image)
        _, bw_image_np = cv2.threshold(image_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        bw_image = Image.fromarray(bw_image_np)

        folder_name = "BnW_Images"
        os.makedirs(folder_name, exist_ok=True)

        bw_image_path = os.path.join(folder_name, f"{self.base_name}_BnW.png")
        bw_image.save(bw_image_path)
        print(f"Black and white image saved at: {bw_image_path}")

    def close_image(self):
        if self.image:
            self.image.close()
