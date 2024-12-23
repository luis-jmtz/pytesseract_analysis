import os
import csv
import pytesseract
from PIL import Image
import pandas as pd

from spacing_analysis import SpacerAnalyzer

base_truth = "AAAA"

# Parameters
input_folder = r"sT_white_space_images"
output_csv = "sT_white_space_analysis.csv"


# Create an instance of OCRAnalyzer
analyzer = SpacerAnalyzer(input_folder, output_csv, base_truth)
analyzer.analyze_images()


# Parameters
input_folder = r"sB_white_space_images"
output_csv = "sB_white_space_analysis.csv"


# Create an instance of OCRAnalyzer
analyzer = SpacerAnalyzer(input_folder, output_csv, base_truth)
analyzer.analyze_images()


# Parameters
input_folder = r"B_white_space_images"
output_csv = "B_white_space_analysis.csv"


# Create an instance of OCRAnalyzer
analyzer = SpacerAnalyzer(input_folder, output_csv, base_truth)
analyzer.analyze_images()



# input_folder = r"white_space_images"
# output_csv = "white_space_analysis.csv"
# base_truth = "AAAA"
# data = []

# for root, dirs, files in os.walk(input_folder):
#     for file in files:
#         if file.endswith(".png"):
#             try:
#                 num_lines = int(file.split("_")[0])  # Extract number of white space lines
#                 image_path = os.path.join(root, file)

#                 img = Image.open(image_path)
#                 detected_text = pytesseract.image_to_string(img).strip()

#                 text_detected = 1 if detected_text else 0

#                 detected_text_array = list(detected_text)
#                 base_truth_array = list(base_truth)

#                 matched_chars = sum(1 for i, char in enumerate(detected_text_array) if i < len(base_truth_array) and char == base_truth_array[i])
#                 accuracy = matched_chars / len(base_truth_array) if base_truth_array else 0

#                 data.append({
#                     "White Space in px": num_lines,
#                     "Text Detected": text_detected,
#                     "OCR Output": detected_text,
#                     "Accuracy": round(accuracy * 100, 2)
#                 })
#             except Exception as e:
#                 print(f"Error processing file {file}: {e}")

# df = pd.DataFrame(data)
# df.to_csv(output_csv, index=False)

# print(f"Processing complete. Data saved to {output_csv}")




# from vertical_white_space import whiteSpacer

# white_space = 1
# spacer = whiteSpacer("Control_Image_cropped.png")


# while white_space < 101:
#     output_file = spacer.add_white_lines(white_space, 2)
#     print(f"Output file: {output_file}")
#     white_space += 1



# from staggered_white_space import staggeredWhiteSpacer

# white_space = 1
# spacer = staggeredWhiteSpacer("Control_Image_cropped.png", "sT_white_space_images")

# while white_space < 101:

#     output_file = spacer.add_staggered_white_lines(white_space, position=1)
#     print(f"Output file: {output_file}")
#     white_space += 1

# white_space = 1
# spacer = staggeredWhiteSpacer("Control_Image_cropped.png", "sB_white_space_images")

# while white_space < 101:

#     output_file = spacer.add_staggered_white_lines(white_space, position=2)
#     print(f"Output file: {output_file}")
#     white_space += 1