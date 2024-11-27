import numpy as np
from PIL import Image
import os

def load_matrix(file_path):
    """Load the matrix from a text file."""
    return np.loadtxt(file_path, dtype=int)

def shift_a_top(matrix, x_shift):
    """
    Shift the tops of the 'A's by x_shift pixels along the x-axis.
    Keep the base of the 'A's fixed while slanting the rest of the A.
    """
    rows, cols = matrix.shape
    base_row = rows - 1  # Assume the last row is the base of the 'A's
    new_matrix = np.ones_like(matrix)  # Start with a blank (white) canvas

    for col in range(cols):
        # Find all points in the column forming the 'A'
        column_points = []
        for row in range(base_row, -1, -1):  # Traverse upwards
            if matrix[row, col] == 0:
                column_points.append((row, col))  # Collect all parts of the 'A'

        if column_points:
            # Base row does not move
            base_x = column_points[0][1]  # x-coordinate of the base
            new_matrix[base_row, base_x] = 0  # Fix the base at the same position

            # Adjust the other points proportionally
            for row, orig_x in column_points[1:]:
                distance_from_base = base_row - row
                proportional_shift = round(x_shift * (distance_from_base / (base_row)))
                new_x = base_x + proportional_shift

                # Ensure new_x is within bounds
                if 0 <= new_x < cols:
                    new_matrix[row, new_x] = 0  # Place the shifted point
    return new_matrix

def save_matrix_as_image(matrix, output_folder, file_name="Transformed_Image.png"):
    """
    Save the matrix as a black-and-white image.
    """
    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Convert matrix to image (invert logic for black text on white background)
    image = Image.fromarray((matrix * 255).astype(np.uint8))  # Convert and cast to uint8
    image_path = os.path.join(output_folder, file_name)
    image.save(image_path)
    print(f"Image saved to {image_path}")

# Input file paths
matrix_path = "Control_Image_Matrix.txt"
output_folder = "output_folder"

# Load the matrix
matrix = load_matrix(matrix_path)

# Define the x-axis shift
x_shift = 10  # Adjust this value to slant more or less

# Transform the matrix
transformed_matrix = shift_a_top(matrix, x_shift)

# Save the transformed matrix as an image
save_matrix_as_image(transformed_matrix, output_folder)
