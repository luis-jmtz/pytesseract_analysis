from letter_image_generator import LetterImageGenerator

def main():
    generator = LetterImageGenerator(
        letter="A",
        num_letters=5,
        letter_spacing=1.5,
        num_iterations=10,
        output_folder="output"
    )
    generator.generate_images()

if __name__ == "__main__":
    main()
