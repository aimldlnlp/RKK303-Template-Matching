import cv2
import numpy as np
import os

# Paths for the PCB image and template folder
pcb_image_path = 'path/to/pcb_image.jpg'
template_folder_path = 'path/to/template_folder'

pcb_image = cv2.imread(pcb_image_path, cv2.IMREAD_GRAYSCALE)
if pcb_image is None:
    raise FileNotFoundError(f"PCB image not found at {pcb_image_path}")

threshold = 0.8
all_rectangles = []

for filename in os.listdir(template_folder_path):
    template_path = os.path.join(template_folder_path, filename)
    if os.path.isfile(template_path) and template_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            continue
        
        template_height, template_width = template.shape
        result = cv2.matchTemplate(pcb_image, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        
        for point in zip(*locations[::-1]):
            all_rectangles.append([int(point[0]), int(point[1]), int(template_width), int(template_height)])
            all_rectangles.append([int(point[0]), int(point[1]), int(template_width), int(template_height)])
