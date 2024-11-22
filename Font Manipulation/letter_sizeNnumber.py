import os
import matplotlib.pyplot as plt

def generate_images(num_letters, letter_spacing, num_iterations, output_folder="output"):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate for each image
    for iteration in range(1, num_iterations + 1):
        # Create a new figure
        fig, ax = plt.subplots(figsize=(5, 5))  # 500x500 px corresponds to a 5x5 inch figure at 100 DPI
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.axis("off")  # Turn off the axis for a clean image

        # Calculate font size and positions
        font_size = iteration  # Use iteration number as font size
        base_spacing = font_size  # The "base" of the A is its font size
        additional_spacing = letter_spacing * base_spacing
        letter_width = base_spacing  # Assume the width of "A" scales proportionally with font size

        # Total width of all letters and spaces
        total_width = num_letters * letter_width + (num_letters - 1) * additional_spacing
        start_x = (500 - total_width) / 2  # Center horizontally
        center_y = 250  # Center vertically

        # Draw the black "A"s
        for i in range(num_letters):
            # Calculate the x position of the current black "A"
            x_position = start_x + i * (letter_width + additional_spacing)
            ax.text(
                x_position,
                center_y,
                "A",
                fontsize=font_size,
                va="center",
                ha="center",
                color="black",
                family="Arial"
            )

        # Save the figure
        output_path = os.path.join(output_folder, f"image_{iteration:03d}.png")
        plt.savefig(output_path, dpi=100, bbox_inches="tight", pad_inches=0)
        plt.close(fig)  # Close the figure to release memory

    print(f"Images saved in folder: {output_folder}")

# Example usage
if __name__ == "__main__":
    generate_images(num_letters=2, letter_spacing=1, num_iterations=25)
