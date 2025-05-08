import os
from PIL import Image

def is_valid_image(file):
    return file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

def resize_image(input_path, output_path, size=(300, 300)):
    with Image.open(input_path) as img:
        img.thumbnail(size)
        img.save(output_path)
