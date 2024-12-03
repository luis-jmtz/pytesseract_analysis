from letter_image_generator_v2 import ImageGenerator
import os
import csv
import pytesseract
from PIL import Image
import pandas as pd

num_letters = 1

while num_letters < 20:
    
    generator = ImageGenerator(
            letter="A",
            num_letters= num_letters,
            letter_spacing=0,
            font_size= 20,
            output_folder="space_tester"
        )

    generator.generate_images()
    
    num_letters += 1