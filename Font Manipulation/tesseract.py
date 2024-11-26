from PIL import Image
import pytesseract

image_path = r"Control_Image_three.png" 

try:
    # Open the image
    img = Image.open(image_path)
    
    # Perform OCR
    text = pytesseract.image_to_string(img)
    
    # Print the extracted text
    print("Extracted Text:")
    print(text)
except Exception as e:
    print(f"An error occurred: {e}")
