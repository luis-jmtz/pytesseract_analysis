from perlin_generator import perlinNoiser

changing_intensity = 0.1


# processor = perlinNoiser("Control_Image.png", changing_intensity,
#     fr"perlin_images1-2\{changing_intensity}_perlin1-2.png")
# processor.process_image()


while changing_intensity <= 0.9:
    
    rounded_intensity = round(changing_intensity, 3)
    
    processor = perlinNoiser("Control_Image.png", rounded_intensity,
    fr"perlin_images1-3\{changing_intensity}_perlin1-3.png")

    processor.process_image()
    
    changing_intensity += 0.1
    


# changing_intensity = 0.1


# while changing_intensity <= 1:
#     processor = perlinNoiser("Control_Image.png", changing_intensity,
#     fr"perlin_images\{changing_intensity}.png")

#     processor.process_image()
    
#     changing_intensity += 0.1