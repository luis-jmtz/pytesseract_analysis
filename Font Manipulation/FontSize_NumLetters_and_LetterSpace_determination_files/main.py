from letter_image_generator import LetterImageGenerator
import os
import csv
import pytesseract
from PIL import Image
import pandas as pd

input_folder = r"Size Number and Spacing Images"
output_csv = "output.csv"

# Initialize an empty list to store the rows for the CSV
data = []

# Loop through all subfolders in the input folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".png"):
            try:
                # Parse the file name
                parts = file.split("_")
                letter = parts[0]
                iteration = int(parts[1])
                num_letters = int(parts[2])
                letter_spacing = int(parts[3].replace(".png", ""))

                # Construct the full path to the image
                image_path = os.path.join(root, file)

                # Open the image and run Tesseract OCR
                img = Image.open(image_path)
                detected_text = pytesseract.image_to_string(img).strip()

                # Determine the "Text Detected" value
                text_detected = 1 if detected_text else 0

                # Append the data to the list
                data.append({
                    "Font Size": iteration,
                    "Number of Letters": num_letters,
                    "Letterspacing": letter_spacing,
                    "Text Detected": text_detected
                })
            except Exception as e:
                print(f"Error processing file {file}: {e}")

# Convert the data to a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Processing complete. Data saved to {output_csv}")




# generator = LetterImageGenerator(
#         letter="A",
#         num_letters=4,
#         letter_spacing=4,
#         num_iterations=50,
#         output_folder="letters4_space4"
#     )

# generator.generate_images()

