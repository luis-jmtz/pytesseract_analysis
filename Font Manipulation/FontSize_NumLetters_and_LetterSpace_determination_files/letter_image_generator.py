import os
import matplotlib.pyplot as plt

class LetterImageGenerator:
    def __init__(self, letter, num_letters, letter_spacing, num_iterations, output_folder):
        # Validate inputs
        if len(letter) != 1:
            raise ValueError("The letter must be a single character.")
        
        self.letter = letter
        self.num_letters = num_letters
        self.letter_spacing = letter_spacing
        self.num_iterations = num_iterations
        self.output_folder = output_folder
        
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_images(self):
        for iteration in range(1, self.num_iterations + 1):
            # Create a new figure
            fig, ax = plt.subplots(figsize=(5, 5), dpi=100)  # 500x500 px
            ax.set_xlim(0, 500)
            ax.set_ylim(0, 500)
            ax.axis("off")  # Turn off the axis for a clean image

            # Calculate font size and positions
            font_size = iteration  # Use iteration number as font size
            base_spacing = font_size  # The "base" of the letter is its font size
            additional_spacing = self.letter_spacing * base_spacing
            letter_width = base_spacing  # Assume the width of the letter scales proportionally with font size

            # Total width of all letters and spaces
            total_width = self.num_letters * letter_width + (self.num_letters - 1) * additional_spacing
            if total_width > 500:
                print(f"Error: The letters would be drawn outside of the grid in iteration {iteration}. Stopping.")
                plt.close(fig)
                return

            start_x = (500 - total_width) / 2  # Center horizontally
            center_y = 250  # Center vertically

            # Draw the letters
            for i in range(self.num_letters):
                # Calculate the x position of the current letter
                x_position = start_x + i * (letter_width + additional_spacing)
                ax.text(
                    x_position,
                    center_y,
                    self.letter,
                    fontsize=font_size,
                    va="center",
                    ha="center",
                    color="black",
                    family="Arial"
                )

            # Save the figure with enforced 500x500 px dimensions
            output_path = os.path.join(
                self.output_folder,
                f"{self.letter}_{iteration}_{self.num_letters}_{self.letter_spacing}.png"
            )
            plt.savefig(output_path, dpi=100, bbox_inches=None, pad_inches=0)
            plt.close(fig)  # Close the figure to release memory

        print(f"Images saved in folder: {self.output_folder}")



'''
import os
import matplotlib.pyplot as plt

def generate_images(
    letter, num_letters, letter_spacing, num_iterations, output_folder
):
    # Validate inputs
    if len(letter) != 1:
        print("Error: The letter must be a single character.")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate for each image
    for iteration in range(1, num_iterations + 1):
        # Create a new figure
        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)  # 500x500 px
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.axis("off")  # Turn off the axis for a clean image

        # Calculate font size and positions
        font_size = iteration  # Use iteration number as font size
        base_spacing = font_size  # The "base" of the letter is its font size
        additional_spacing = letter_spacing * base_spacing
        letter_width = base_spacing  # Assume the width of the letter scales proportionally with font size

        # Total width of all letters and spaces
        total_width = num_letters * letter_width + (num_letters - 1) * additional_spacing
        if total_width > 500:
            print("Error: The letters would be drawn outside of the grid. Stopping.")
            plt.close(fig)
            return

        start_x = (500 - total_width) / 2  # Center horizontally
        center_y = 250  # Center vertically

        # Draw the letters
        for i in range(num_letters):
            # Calculate the x position of the current letter
            x_position = start_x + i * (letter_width + additional_spacing)
            ax.text(
                x_position,
                center_y,
                letter,
                fontsize=font_size,
                va="center",
                ha="center",
                color="black",
                family="Arial"
            )

        # Save the figure with enforced 500x500 px dimensions
        output_path = os.path.join(
            output_folder,
            f"{letter}_{iteration}_{num_letters}_{letter_spacing}.png"
        )
        plt.savefig(output_path, dpi=100, bbox_inches=None, pad_inches=0)
        plt.close(fig)  # Close the figure to release memory

    print(f"Images saved in folder: {output_folder}")

# Example usage
if __name__ == "__main__":
    generate_images(
        letter="A",
        num_letters=5,
        letter_spacing=1.5,
        num_iterations=10,
        output_folder="output3"
    )
'''