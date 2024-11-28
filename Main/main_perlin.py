from perlin_generator import perlinNoiser

changing_intensity = 0.2


while changing_intensity < .3:
    
    rounded_intensity = round(changing_intensity, 3)
    
    processor = perlinNoiser("Control_Image.png", rounded_intensity,
    fr"perlin_images2-1\{changing_intensity}_perlin2-1.png")

    processor.process_image()
    
    changing_intensity += 0.01
    


# changing_intensity = 0.1


# while changing_intensity <= 1:
#     processor = perlinNoiser("Control_Image.png", changing_intensity,
#     fr"perlin_images\{changing_intensity}.png")

#     processor.process_image()
    
#     changing_intensity += 0.1