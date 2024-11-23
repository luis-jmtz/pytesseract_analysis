import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Define the output folder
output_folder = "image_processing_results"
os.makedirs(output_folder, exist_ok=True)

def process_image(image_path):
    # Load the image
    image = Image.open(image_path).convert("1")  # Convert to 1-bit pixels (black and white)
    
    # Save the bitmap
    bitmap_path = os.path.join(output_folder, "bitmap.bmp")
    image.save(bitmap_path)
    
    # Convert to a numpy matrix
    matrix = np.array(image, dtype=int)  # 0 for white, 1 for black
    
    # Save the matrix to a text file
    matrix_path = os.path.join(output_folder, "matrix.txt")
    np.savetxt(matrix_path, matrix, fmt='%d')
    
    # Plot the grid using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='gray', interpolation='nearest')
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
    ax.grid(which='minor', color='red', linestyle='-', linewidth=0.5)
    ax.tick_params(which="minor", size=0)
    plt.axis('off')
    
    # Save the grid visualization
    grid_path = os.path.join(output_folder, "grid.png")
    plt.savefig(grid_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    
    return bitmap_path, matrix_path, grid_path

# Example usage
image_path = "Control_Image.png"
bitmap, matrix, grid = process_image(image_path)
(bitmap, matrix, grid)
