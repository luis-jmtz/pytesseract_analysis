from perlin_generator import perlinNoiser

changing_intensity = 0.219


while changing_intensity < 0.23:
    
    # rounded_intensity = round(changing_intensity, 5)
    
    processor = perlinNoiser("Control_Image.png", round(changing_intensity, 5),
    fr"perlin_images2-2\{round(changing_intensity, 5)}_perlin2-2.png")

    processor.process_image()
    
    changing_intensity += 0.001