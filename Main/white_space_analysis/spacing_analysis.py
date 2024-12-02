import os
import pandas as pd
from PIL import Image
import pytesseract

class SpacerAnalyzer:
    def __init__(self, input_folder, output_csv, base_truth):

        self.input_folder = input_folder
        self.output_csv = output_csv
        self.base_truth = base_truth

    def analyze_images(self):

        data = []

        for root, dirs, files in os.walk(self.input_folder):
            for file in files:
                if file.endswith(".png"):
                    try:
                        num_lines = int(file.split("_")[0])  # Extract number of white space lines
                        image_path = os.path.join(root, file)

                        img = Image.open(image_path)
                        detected_text = pytesseract.image_to_string(img).strip()

                        text_detected = 1 if detected_text else 0

                        detected_text_array = list(detected_text)
                        base_truth_array = list(self.base_truth)

                        matched_chars = sum(1 for i, char in enumerate(detected_text_array) 
                                            if i < len(base_truth_array) and char == base_truth_array[i])
                        accuracy = matched_chars / len(base_truth_array) if base_truth_array else 0

                        data.append({
                            "White Space in px": num_lines,
                            "Text Detected": text_detected,
                            "OCR Output": detected_text,
                            "Accuracy": round(accuracy * 100, 2)
                        })
                    except Exception as e:
                        print(f"Error processing file {file}: {e}")

        # Save results to CSV
        df = pd.DataFrame(data)
        df.to_csv(self.output_csv, index=False)
        print(f"Processing complete. Data saved to {self.output_csv}")
