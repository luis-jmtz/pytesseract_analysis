from letter_image_generator_v2 import ImageGenerator
import os
import csv
import pytesseract
from PIL import Image
import pandas as pd
num_letters = 1
letter_space = 0


# turns out I made a mistake and I didn't need to make the Space and Number file


# while num_letters < 20:
    
#     generator = ImageGenerator(
#             letter="A",
#             num_letters= num_letters,
#             letter_spacing= letter_space,
#             font_size= 20,
#             output_folder= r"Space and Number\f1"
#         )

#     generator.generate_images()
    
#     num_letters += 1


while letter_space <7:
    
    while num_letters < 21:
    
        generator = ImageGenerator(
                letter="A",
                num_letters= num_letters,
                letter_spacing= letter_space,
                font_size= 20,
                output_folder= fr"Space and Number\space{letter_space}"
            )

        generator.generate_images()
        
        num_letters += 1
        
    letter_space +=1
    num_letters = 1
