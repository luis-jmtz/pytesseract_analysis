import os
import csv
import pytesseract
from PIL import Image
import pandas as pd




from vertical_white_space import whiteSpacer

white_space = 1
spacer = whiteSpacer("Control_Image_cropped.png")


while white_space < 3:
    output_file = spacer.add_white_lines(white_space, 1)
    print(f"Output file: {output_file}")
    white_space += 1









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






