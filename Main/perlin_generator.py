from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class perlinNoiser:
    def __init__(self, input_image_path, intensity, output_image_path):
        self.input_image_path = input_image_path
        self.intensity = intensity
        self.output_image_path = output_image_path

    def generate_perlin_noise(self, width, height, scale=100):
        def lerp(a, b, t):
            return a + t * (b - a)
        
        def fade(t):
            return t * t * t * (t * (t * 6 - 15) + 10)
        
        def gradient(h, x, y):
            # Gradient vectors (simplified for 2D Perlin Noise)
            vectors = np.array([[1, 1], [-1, 1], [1, -1], [-1, -1]])
            return vectors[h % 4, 0] * x + vectors[h % 4, 1] * y
        
        def perlin(x, y):
            # Determine grid cell coordinates
            x0, y0 = int(np.floor(x)), int(np.floor(y))
            x1, y1 = x0 + 1, y0 + 1
            
            # Relative coordinates
            sx, sy = x - x0, y - y0
            
            # Fade curves
            u, v = fade(sx), fade(sy)
            
            # Gradient hashes
            g00 = gradient(np.random.randint(0, 4), sx, sy)
            g01 = gradient(np.random.randint(0, 4), sx, sy - 1)
            g10 = gradient(np.random.randint(0, 4), sx - 1, sy)
            g11 = gradient(np.random.randint(0, 4), sx - 1, sy - 1)
            
            # Interpolate
            nx0 = lerp(g00, g10, u)
            nx1 = lerp(g01, g11, u)
            nxy = lerp(nx0, nx1, v)
            return nxy
        
        noise = np.zeros((height, width))
        for y in range(height):
            for x in range(width):
                noise[y, x] = perlin(x / scale, y / scale)
        
        # Normalize
        noise = (noise - noise.min()) / (noise.max() - noise.min()) * 255
        return noise.astype(np.uint8)

    def process_image(self):
        # Load the input image
        image = Image.open(self.input_image_path).convert("L")
        image_array = np.array(image)
        
        # Generate Perlin noise
        noise = self.generate_perlin_noise(image_array.shape[1], image_array.shape[0])
        
        # Blend the image with noise
        blended = ((1 - self.intensity) * image_array + self.intensity * noise).astype(np.uint8)
        
        # Save the result
        output_image = Image.fromarray(blended)
        output_image.save(self.output_image_path)