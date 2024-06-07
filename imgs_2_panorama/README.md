# imgs_2_panorama

## Overview
This project was created as part of an assignment in a Graphics Programming class, focusing on using Python and various libraries to achieve different computer vision effects and functions. The goal of the project was to combine three overlapping images into a single panoramic image without reducing the size of the original images.

For an in-depth breakdown of the code, please read the presentation found at 'imgs_2_panorama.pdf'

## Features
- Uses NumPy and OpenCV libraries for image processing.
- Combines multiple images into a seamless panorama.
- Handles keypoint detection and matching.
- Crops the final panorama to remove excess black space.

## Getting Started

### Prerequisites
- Python 3.6 or higher.
- An Integrated Development Environment (IDE) like Visual Studio Code.
- NumPy library.
- OpenCV library.

### Installation
Clone the repository:

git clone https://github.com/qmmartin/Portfolio

Open the project in your preferred IDE.

### Running the Project
1. Open the 'imgs_2_panorama' folder in Visual Studio or other IDE
2. Run pano.py

### How It Works
1. Keypoint Matching:
   - The script first creates keypoint matches between the leftmost and center images, as well as between the center and rightmost images.

        <img src="output_imgs\matches.png" width="400">

2. Image Translation:
   - Using the keypoints, the script determines the correct placement of each image on a new canvas.

        <img src="output_imgs\out1.png" width="400">  <img src="output_imgs\out2.png" width="400">  <img src="output_imgs\out3.png" width="400">

3. Image Merging:
   - Masks are created to blend the overlapping sections of the images, preventing pixel overlap and discoloration.

        <img src="output_imgs\panoFinal.png" width="400">

4. Cropping:
   - The final panorama is cropped to remove excess black space, resulting in the final panoramic image.

        <img src="output_imgs\cropped_panoFinal.png" width="400">