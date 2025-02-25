"""
Filename: img_transforms.py
Author: WormStan
Date: 2/18/2025
Description: Toolktis for augment image as training data
"""

import cv2
import albumentations as A
import os
import random


class IMG_Transforms:
    def __init__(self):
        # Define augmentations
        self.augmentations = A.Compose([
            # A.Rotate(limit=30, p=0.5),
            A.RandomScale(scale_limit=0.5, p=0.5),
            # A.RandomBrightnessContrast(p=0.5),
            # A.HorizontalFlip(p=0.5),
        ])

    def _augment_image(self, image):
        augmented = self.augmentations(image=image)
        return augmented['image']

    def _composite_image(foreground, background):
        fg_h, fg_w, _ = foreground.shape
        bg_h, bg_w, _ = background.shape

        # Generate random position for the foreground image on the background
        x_offset = random.randint(0, bg_w - fg_w)
        y_offset = random.randint(0, bg_h - fg_h)

        # Create an alpha mask
        alpha = foreground[:, :, 3] / 255.0
        foreground = foreground[:, :, :3]

        # Composite the images at the random position
        for c in range(0, 3):
            background[y_offset:y_offset+fg_h, x_offset:x_offset+fg_w, c] = (
                alpha * foreground[:, :, c] +
                (1 - alpha) *
                background[y_offset:y_offset+fg_h, x_offset:x_offset+fg_w, c]
            )

        return background

    def image_transform(self, icon_path, backgroud_path, output_dir,count=30):
        # Generate augmented images
        output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

        for i in range(count):  # Generated number of augmented images
            # Load your icon image (with alpha channel for transparency)
            icon_path = icon_path
            icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
            # Load a background image
            background_path = backgroud_path
            background = cv2.imread(background_path)
            augmented_icon = self._augment_image(icon)
            composite = self._composite_image(augmented_icon, background)
            output_path = os.path.join(output_dir, f'augmented_{i}.png')
            cv2.imwrite(output_path, composite)

        print("Data generation complete.")
