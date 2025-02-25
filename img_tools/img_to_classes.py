"""
Filename: img_to_classes.py
Author: WormStan
Date: 2/18/2025
Description: Toolktis for list image name to YOLO classes
"""


import os


def list_png_files(directory, output_file):
    """
    List all PNG files in the specified directory and write their filenames to a text file.

    :param directory: Directory containing PNG files.
    :param output_file: Path to the output text file.
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Filter out files that end with .png
    png_files = [os.path.splitext(file)[0] for file in files if file.endswith('.png')]

    # Write the filenames to the output text file
    with open(output_file, 'w') as f:
        for png_file in png_files:
            f.write(png_file + '\n')


# Example usage
# Replace with your directory containing PNG files
directory = r"C:\Temp\PNGs"
# Replace with your desired output text file path
output_file = r"C:\Temp\PNGs\output.txt"
list_png_files(directory, output_file)
