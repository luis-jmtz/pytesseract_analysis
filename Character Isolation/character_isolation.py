import cv2
import numpy as np
import os

def isolate_characters(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # List to hold individual character images
    character_images = []
    
    # Loop through contours and extract bounding boxes
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Print the coordinates of the bounding box
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        print(f"Top-left: {top_left}, Bottom-right: {bottom_right}")
        
        # Extract the character by cropping the bounding box region
        character_image = image[y:y+h, x:x+w]
        character_images.append(character_image)
        
        # Draw a thin bounding box on the original image for visualization
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1)
    
    # Save the processed image with bounding boxes
    base_name = os.path.splitext(os.path.basename(image_path))[0]  # Get base file name
    new_image_path = f"{base_name}_character_boxes.png"
    cv2.imwrite(new_image_path, image)
    print(f"Image saved as {new_image_path}")
    
    # Show the processed image with bounding boxes (optional)
    cv2.imshow("Characters Isolated", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return character_images  # Returns list of isolated character images

isolated_characters = isolate_characters(r'times new roman bold italic.png')
