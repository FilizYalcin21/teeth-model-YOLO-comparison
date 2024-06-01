# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:50:45 2024

@author: filiz
"""
import os

def convert_to_yolo_format(image_width, image_height, annotations, class_label):
    yolo_annotations = []

    for (x_min, y_min, x_max, y_max) in annotations:
        # Calculate center of the bounding box
        x_center = (x_min + x_max) / 2.0
        y_center = (y_min + y_max) / 2.0

        # Calculate width and height of the bounding box
        bbox_width = x_max - x_min
        bbox_height = y_max - y_min

        # Normalize the coordinates by the dimensions of the image
        x_center /= image_width
        y_center /= image_height
        bbox_width /= image_width
        bbox_height /= image_height

        # Append the annotation in YOLO format
        yolo_annotations.append(f"{class_label} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")

    return yolo_annotations

def read_annotations(file_path):
    annotations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            x_min, y_min, x_max, y_max = map(float, line.strip().split())
            annotations.append((x_min, y_min, x_max, y_max))
    return annotations

def write_yolo_annotations(file_path, yolo_annotations):
    with open(file_path, 'w') as file:
        for annotation in yolo_annotations:
            file.write(annotation + "\n")

def process_files(teeth_dir, caries_dir, output_dir, image_width, image_height):
    for file_name in os.listdir(teeth_dir):
        if file_name.endswith(".txt"):
            teeth_file_path = os.path.join(teeth_dir, file_name)
            caries_file_path = os.path.join(caries_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            combined_annotations = []

            # Read teeth annotations
            if os.path.exists(teeth_file_path):
                teeth_annotations = read_annotations(teeth_file_path)
                combined_annotations.extend(convert_to_yolo_format(image_width, image_height, teeth_annotations, class_label=0))

            # Read caries annotations
            if os.path.exists(caries_file_path):
                caries_annotations = read_annotations(caries_file_path)
                combined_annotations.extend(convert_to_yolo_format(image_width, image_height, caries_annotations, class_label=1))

            # Write combined annotations to output file
            write_yolo_annotations(output_file_path, combined_annotations)

# Set the image dimensions
image_width = 2943
image_height = 1435

# Define input directories for teeth and caries annotations
caries_dir = 'C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/panoramic dental dataset/annotations/bboxes_caries'
teeth_dir = 'C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/panoramic dental dataset/annotations/bboxes_teeth'
output_dir = 'C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/yolo annotation/teeth-and-caries'

# Define output directory for combined YOLO formatted annotations
os.makedirs(output_dir, exist_ok=True)

# Process files and generate combined YOLO formatted annotations
process_files(teeth_dir, caries_dir, output_dir, image_width, image_height)
