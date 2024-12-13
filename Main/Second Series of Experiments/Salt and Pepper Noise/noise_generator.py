import cv2
import numpy as np

class noiseMaker:
    def __init__(self, strength=0.01):

        if not (0 <= strength <= 1):
            raise ValueError("Strength must be between 0 and 1.")
        self.strength = strength

    def apply_noise(self, image_path):

        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ValueError("Invalid image path.")
        
        # Copy the image to add noise
        noisy_image = image.copy()
        h, w = image.shape[:2]  # Image dimensions
        total_pixels = h * w  # Total number of pixels in the image
        
        # Number of pixels to alter
        num_salt = int(total_pixels * self.strength / 2)
        num_pepper = int(total_pixels * self.strength / 2)
        
        # Add salt noise (white pixels)
        coords_salt = np.random.randint(0, h, num_salt), np.random.randint(0, w, num_salt)
        if len(image.shape) == 2:  # Grayscale
            noisy_image[coords_salt] = 255
        else:  # Color image
            noisy_image[coords_salt[0], coords_salt[1], :] = 255  # All channels set to white
        
        # Add pepper noise (black pixels)
        coords_pepper = np.random.randint(0, h, num_pepper), np.random.randint(0, w, num_pepper)
        if len(image.shape) == 2:  # Grayscale
            noisy_image[coords_pepper] = 0
        else:  # Color image
            noisy_image[coords_pepper[0], coords_pepper[1], :] = 0  # All channels set to black
        
        return noisy_image

    def save_image(self, image, output_path):

        cv2.imwrite(output_path, image)

    def process_and_save(self, image_path):

        noisy_image = self.apply_noise(image_path)
        output_path = fr"noisy_images_v2-3\{self.strength}_SnP.png"
        self.save_image(noisy_image, output_path)
        print(f"Noisy image: {output_path}")
