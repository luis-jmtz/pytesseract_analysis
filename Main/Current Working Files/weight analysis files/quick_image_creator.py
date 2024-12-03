import os
import matplotlib.pyplot as plt

class LetterImageGenerator:
    def __init__(self, letter, num_letters, letter_spacing, font_size, output_folder):
        # Validate inputs
        if len(letter) != 1:
            raise ValueError("The letter must be a single character.")
        
        self.letter = letter
        self.num_letters = num_letters
        self.letter_spacing = letter_spacing
        self.font_size = font_size
        self.output_folder = output_folder
        
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_images(self):
        # Create a new figure
        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)  # 500x500 px
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.axis("off")  # Turn off the axis for a clean image

        # Calculate positions based on the font size
        base_spacing = self.font_size  # The "base" of the letter is its font size
        additional_spacing = self.letter_spacing * base_spacing
        letter_width = base_spacing  # Assume the width of the letter scales proportionally with font size

        # Total width of all letters and spaces
        total_width = self.num_letters * letter_width + (self.num_letters - 1) * additional_spacing
        if total_width > 500:
            print("Error: The letters would be drawn outside of the grid. Adjust font size or letter spacing.")
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
                fontsize=self.font_size,
                va="center",
                ha="center",
                color="black",
                family="Arial"
            )

        # Save the figure with enforced 500x500 px dimensions
        output_path = os.path.join(
            self.output_folder,
            f"{self.letter}_{self.num_letters}_{self.letter_spacing}_{self.font_size}.png"
        )
        plt.savefig(output_path, dpi=100, bbox_inches=None, pad_inches=0)
        plt.close(fig)  # Close the figure to release memory

        print(f"Image saved in folder: {self.output_folder}")



if __name__ == "__main__":
    generator = LetterImageGenerator(
        letter="A",
        num_letters=4,
        letter_spacing=1,
        font_size=70,
        output_folder="temp"
    )
    generator.generate_images()
