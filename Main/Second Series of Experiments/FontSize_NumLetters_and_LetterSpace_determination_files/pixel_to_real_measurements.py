# Constants
DPI = 100
MM_PER_INCH = 25.4
CM_PER_INCH = 2.54

# Input: pixel height
pixel_height = 20

# Convert to inches, mm, and cm
height_in_inches = pixel_height / DPI
height_in_mm = height_in_inches * MM_PER_INCH
height_in_cm = height_in_inches * CM_PER_INCH

# Print the results
print(f"Pixel height: {pixel_height}px")
print(f"Height in inches: {height_in_inches:.2f} inches")
print(f"Height in millimeters: {height_in_mm:.2f} mm")
print(f"Height in centimeters: {height_in_cm:.2f} cm")
