import os
import cv2
import numpy as np
import pandas as pd
from glob import glob

def analyze_character(image_path):

    # Read image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    
    # Calculate contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Line thickness
    thicknesses = []
    for contour in contours:
        for i in range(len(contour) - 1):
            pt1, pt2 = contour[i][0], contour[i + 1][0]
            thickness = np.linalg.norm(pt1 - pt2)
            thicknesses.append(thickness)
    
    avg_thickness = np.mean(thicknesses) if thicknesses else 0
    min_thickness = np.min(thicknesses) if thicknesses else 0
    max_thickness = np.max(thicknesses) if thicknesses else 0

    # Line angles
    angles = []
    for contour in contours:
        for i in range(len(contour) - 1):
            pt1, pt2 = contour[i][0], contour[i + 1][0]
            dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
            angle = np.arctan2(dy, dx) * (180.0 / np.pi)  # Convert to degrees
            angles.append(angle)
    
    avg_angle_to_bottom = np.mean([abs(angle) for angle in angles]) if angles else 0
    min_angle_to_bottom = np.min([abs(angle) for angle in angles]) if angles else 0
    max_angle_to_bottom = np.max([abs(angle) for angle in angles]) if angles else 0

    avg_angle_between_lines = np.mean(np.diff(angles)) if len(angles) > 1 else 0
    min_angle_between_lines = np.min(np.diff(angles)) if len(np.diff(angles)) > 0 else 0
    max_angle_between_lines = np.max(np.diff(angles)) if len(np.diff(angles)) > 0 else 0

    # Count curves
    angle_diffs = np.diff(angles)
    num_curves = len([1 for diff in angle_diffs if abs(diff) > 15])  # Curves when angle change is large
    
    return {
        "avg_thickness (px)": avg_thickness,
        "min_thickness (px)": min_thickness,
        "max_thickness (px)": max_thickness,
        "avg_angle_to_bottom (deg)": avg_angle_to_bottom,
        "min_angle_to_bottom (deg)": min_angle_to_bottom,
        "max_angle_to_bottom (deg)": max_angle_to_bottom,
        "avg_angle_between_lines (deg)": avg_angle_between_lines,
        "min_angle_between_lines (deg)": min_angle_between_lines,
        "max_angle_between_lines (deg)": max_angle_between_lines,
        "avg_num_curves": num_curves
    }

def analyze_font(font_folder):

    results = {
        "avg_thickness (px)": [],
        "min_thickness (px)": [],
        "max_thickness (px)": [],
        "avg_angle_to_bottom (deg)": [],
        "min_angle_to_bottom (deg)": [],
        "max_angle_to_bottom (deg)": [],
        "avg_angle_between_lines (deg)": [],
        "min_angle_between_lines (deg)": [],
        "max_angle_between_lines (deg)": [],
        "avg_num_curves": []
    }
    
    # Loop over each character image in the folder
    for img_path in glob(os.path.join(font_folder, "*.png")):
        char_results = analyze_character(img_path)
        for key, value in char_results.items():
            results[key].append(value)
    
    # Aggregate results for the font
    return {
        "font": os.path.basename(font_folder),
        "avg_thickness (px)": np.mean(results["avg_thickness (px)"]),
        "min_thickness (px)": np.min(results["min_thickness (px)"]),
        "max_thickness (px)": np.max(results["max_thickness (px)"]),
        "avg_angle_to_bottom (deg)": np.mean(results["avg_angle_to_bottom (deg)"]),
        "min_angle_to_bottom (deg)": np.min(results["min_angle_to_bottom (deg)"]),
        "max_angle_to_bottom (deg)": np.max(results["max_angle_to_bottom (deg)"]),
        "avg_angle_between_lines (deg)": np.mean(results["avg_angle_between_lines (deg)"]),
        "min_angle_between_lines (deg)": np.min(results["min_angle_between_lines (deg)"]),
        "max_angle_between_lines (deg)": np.max(results["max_angle_between_lines (deg)"]),
        "avg_num_curves": np.mean(results["avg_num_curves"])
    }

def analyze_fonts_in_folder(fonts_folder):

    analysis_results = []
    
    # Loop over each font folder in the base folder
    for font_folder in os.listdir(fonts_folder):
        font_path = os.path.join(fonts_folder, font_folder)
        if os.path.isdir(font_path):
            print(f"Analyzing font: {font_folder}")
            font_results = analyze_font(font_path)
            analysis_results.append(font_results)
    
    # Save results to a CSV
    df = pd.DataFrame(analysis_results)
    df.to_csv("all_ font_analysis.csv", index=False)

# Specify the path to the folder containing folders of font images
fonts_folder = r"all_Font_Image_Folder"  # Path where each font folder is located

# Run the analysis
analyze_fonts_in_folder(fonts_folder)
