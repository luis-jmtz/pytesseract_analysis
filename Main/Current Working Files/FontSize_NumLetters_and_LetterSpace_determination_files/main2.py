from letter_image_generator_v2 import ImageGenerator
import os
import csv
import pytesseract
from PIL import Image
import pandas as pd

generator = ImageGenerator(
        letter="A",
        num_letters=4,
        letter_spacing=4,
        font_size= 20,
        output_folder="letters4_space4"
    )

generator.generate_images()