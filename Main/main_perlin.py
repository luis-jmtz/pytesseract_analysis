from perlin_generator import perlinNoiser

changing_intensity = 0.9


processor = perlinNoiser("Control_Image.png", changing_intensity,
fr"perlin_images\{changing_intensity}.png")

processor.process_image()


# while changing_intensity <= 0.1:
#     processor = perlinNoiser("Control_Image.png", changing_intensity,
#     fr"perlin_images\{changing_intensity}.png")

#     processor.process_image()
    
#     changing_intensity += 0.01

# changing_intensity = 0.1


# while changing_intensity <= 1:
#     processor = perlinNoiser("Control_Image.png", changing_intensity,
#     fr"perlin_images\{changing_intensity}.png")

#     processor.process_image()
    
#     changing_intensity += 0.1