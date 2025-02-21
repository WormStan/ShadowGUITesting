"""
Filename: svg_converter.py
Author: WormStan
Date: 2/18/2025
Description: Toolktis for convert SVG picture to PNG format
"""

from cairosvg import svg2png
import os


class SvgConverter:
    def __init__(self, output_directory=None):
        """
        Initialize the SvgConverter with an optional output directory.

        :param output_directory: Directory where the PNG files will be saved. If None, saves in the same directory as the SVG file.
        """
        self.output_directory = output_directory

    def convert_svg_file_to_png(self, svg_file):
        """
        Convert an SVG file to a PNG file with the same name.

        :param svg_file: Path to the SVG file to be converted.
        """
        # Read the SVG content from the file
        with open(svg_file, 'r',encoding='utf-8') as file:
            svg_content = file.read()

        # Generate the output PNG file name
        output_file = os.path.splitext(os.path.basename(svg_file))[0] + ".png"
        if self.output_directory:
            output_file = os.path.join(self.output_directory, output_file)
        else:
            output_file = os.path.splitext(svg_file)[0] + ".png"

        # Convert SVG to PNG
        svg2png(bytestring=svg_content.encode('utf-8'), write_to=output_file)

        print(
            f"SVG file '{svg_file}' has been successfully converted to '{output_file}'.")

    def convert_all_svgs_in_directory(self, directory):
        """
        Convert all SVG files in a directory to PNG files.

        :param directory: Directory containing SVG files.
        :param output_directory: Directory where the PNG files will be saved. If None, saves in the same directory as the SVG files.
        """

        for filename in os.listdir(directory):
            if filename.endswith(".svg"):
                svg_file = os.path.join(directory, filename)
                self.convert_svg_file_to_png(svg_file)
