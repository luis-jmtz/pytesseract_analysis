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
        letter_width = font_size  # Assume width of "A" is proportional to its font size
        total_width = num_letters * letter_width + (num_letters - 1) * max(letter_spacing, 0)
        start_x = (500 - total_width) / 2  # Center horizontally
        center_y = 250  # Center vertically

        # Draw the letters
        for i in range(num_letters):
            # Position for the black "A"
            x_position = start_x + i * (letter_width + max(letter_spacing, 0))
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

            # Position and draw the white "A" for spacing if letter_spacing > 0
            if i < num_letters - 1 and letter_spacing > 0:
                x_position_spacing = x_position + letter_width
                ax.text(
                    x_position_spacing,
                    center_y,
                    "A",
                    fontsize=font_size,
                    va="center",
                    ha="center",
                    color="white",
                    family="Arial"
                )

        # Save the figure
        output_path = os.path.join(output_folder, f"image_{iteration:03d}.png")
        plt.savefig(output_path, dpi=100, bbox_inches="tight", pad_inches=0)
        plt.close(fig)  # Close the figure to release memory

    print(f"Images saved in folder: {output_folder}")

# Example usage
if __name__ == "__main__":
    generate_images(num_letters=5, letter_spacing=10, num_iterations=10)
