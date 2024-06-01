# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:44:17 2024

@author: filiz
"""
import os
import random
from shutil import copyfile

# Define paths for your dataset and where to save the split datasets
dataset_dir = "C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/panoramic dental dataset/images"
train_dir = "C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/datasets/teeth/train/images"
val_dir = "C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/datasets/teeth/valid/images"
test_dir = "C:/Users/lenovo/OneDrive/Masaüstü/ders/Yapay Zekâya Giriş/dönem projesi/datasets/teeth/test/images"

# Create directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# List all images in your dataset directory
images = os.listdir(dataset_dir)

# Define the split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Calculate the number of images for each split
num_images = len(images)
num_train = int(train_ratio * num_images)
num_val = int(val_ratio * num_images)
num_test = num_images - num_train - num_val

# Shuffle the images list randomly
random.shuffle(images)

# Split the images into train, val, and test sets
train_images = images[:num_train]
val_images = images[num_train:num_train+num_val]
test_images = images[num_train+num_val:]

# Copy images to their respective directories
def copy_images(image_list, src_dir, dest_dir):
    for image in image_list:
        src_path = os.path.join(src_dir, image)
        dest_path = os.path.join(dest_dir, image)
        copyfile(src_path, dest_path)

copy_images(train_images, dataset_dir, train_dir)
copy_images(val_images, dataset_dir, val_dir)
copy_images(test_images, dataset_dir, test_dir)

print("Dataset split completed!")
print("Train set size:", len(train_images))
print("Validation set size:", len(val_images))
print("Test set size:", len(test_images))
