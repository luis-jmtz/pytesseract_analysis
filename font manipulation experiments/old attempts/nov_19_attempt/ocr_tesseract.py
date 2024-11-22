import os
import pytesseract
from PIL import Image


class TesseractOCR:
    def __init__(self, input_folder, ground_truth="A"):
        """
        Initializes the OCR processor.

        Parameters:
            input_folder (str): Path to the folder containing PNG files.
            ground_truth (str): The expected text for OCR recognition.
        """
        self.input_folder = input_folder
        self.ground_truth = ground_truth

    def process_all(self):
        """
        Processes all PNG files in the input folder, performs OCR, and compares the result with the ground truth.
        """
        # Get a list of all PNG files in the input folder
        png_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.png')]

        for png_file in png_files:
            # Construct the full path to the PNG file
            input_path = os.path.join(self.input_folder, png_file)

            # Perform OCR on the image
            recognized_text = self.perform_ocr(input_path)

            # Extract parameters from the file name
            parameters = self.extract_parameters(png_file)

            # Compare the recognized text with the ground truth
            if recognized_text == self.ground_truth:
                print(f"Tesseract is correct at weight value {parameters['weight']}, "
                      f"Slant {parameters['slant']} Degrees, and Width {parameters['width']}.")
            else:
                print(f"Tesseract is incorrect at weight value {parameters['weight']}, "
                      f"Slant {parameters['slant']} Degrees, and Width {parameters['width']}.")

    def perform_ocr(self, image_path):
        """
        Performs OCR on a single image using Tesseract.

        Parameters:
            image_path (str): Path to the image file.

        Returns:
            str: The recognized text.
        """
        image = Image.open(image_path)
        return pytesseract.image_to_string(image, lang='eng').strip()

    def extract_parameters(self, file_name):
        """
        Extracts parameters (weight, slant, width) from the file name.

        Parameters:
            file_name (str): The name of the PNG file.

        Returns:
            dict: A dictionary with keys 'weight', 'slant', and 'width'.
        """
        # Example file name format: "weight400_slant0_width0.png"
        base_name = os.path.splitext(file_name)[0]
        parts = base_name.split('_')

        parameters = {
            'weight': int(parts[0].replace('weight', '')),
            'slant': int(parts[1].replace('slant', '')),
            'width': int(parts[2].replace('width', ''))
        }

        return parameters
