from perlin_noise import PerlinNoise
from PIL import Image
import numpy as np


class perlinNoiser:
    def __init__(self, input_image_path, intensity, output_image_path):
        self.input_image_path = input_image_path
        self.intensity = intensity
        self.output_image_path = output_image_path

    def generate_perlin_noise(self, width, height, octaves=6):
        noise = PerlinNoise(octaves=octaves, seed=42)
        # Generate noise values for each pixel
        pic = [[noise([i / width, j / height]) for j in range(width)] for i in range(height)]
        pic = np.array(pic)
        # Normalize the noise to fit into 0-255
        pic = (pic - pic.min()) / (pic.max() - pic.min()) * 255
        print("Noise generated")
        return pic.astype(np.uint8)

    def process_image(self):
        # Load the input image
        image = Image.open(self.input_image_path).convert("L")  # Convert to grayscale
        image_array = np.array(image)
        print("Image Loaded")

        # Generate Perlin noise with the same dimensions as the image
        noise = self.generate_perlin_noise(image_array.shape[1], image_array.shape[0])

        # Blend the image with the Perlin noise
        blended = ((1 - self.intensity) * image_array + self.intensity * noise).astype(np.uint8)

        # Save the result
        output_image = Image.fromarray(blended)
        output_image.save(self.output_image_path)