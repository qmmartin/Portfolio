# Using Stable Diffusion's Variational Autoencoders for Lossy Image Compression.

## Overview

This project was originally created as a year long research project to be presented at the West Central Regional Science fair competition at the Arkansas School for Mathematics, Sciences, and the Arts.

This project is a python-based program that utilizies Stable Diffusion's Variational Autoencoder (VAE) to compress images. The images are then analyzed and graded based on their accuracy to the original, and these scores are used to form an accurate analysis of the specific model's compression quality.

<img src="images\vae_example.png" width="600">

RunwayML's Stable Diffusion v1.5 was utilized for the purposes of this project, specifically the lower storage-intensive 'pruned-emaonly' weight.

The scalar used frequently in the code is from [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) and serves as the inverse standard deviation for the latents of the Variational Autoencoder used in Stable Diffusion 1.5.

The paper found within this file at 'lossy_image_compression_paper.pdf' presents much more information than is easily shown within a markdown file. Please read the paper for further information on the project.

## Features
- Img2img VAE compression
- PNG compression
- WebP compression
- File size reduction 
- Latent representation
- Image Quality Assessments
  - Structural Similarity Index 
  - Mean Squared Error
  - Peak-Signal-to-Noise Ratio
  

## Getting Started

###  Prerequisites
- An Integrated Development Environment (IDE) like Visual Studio Code.
- Python 3.6 or higher
- OpenCV Library
- NumPy Library
- Diffusers Library
- Transformers Library
- FastDownload Library
- Pandas Library
- PyTorch Library
- Matplot Library

### Python Scripts
- main.py: The main script; Used to run the other modules.
- vae_module.py: Contains the functions that allow for VAE compression
- friqa_module.py: Contains the functions that allow for Image Quality Assessments

### Installation
Clone the repository:

git clone https://github.com/qmmartin/Portfolio

Open the project in your preferred IDE.

### Running the Code

 ***Important: Running this code will automatically download the Safetensors model used to handle the VAE Compression. This may take some time.**
1. Open the 'img_compression_research_project' folder in Visual Studio or other IDE
2. Run 'main.py' **Important: This will overwrite any images in the output folder found on the original repository. This may take some time**

### How It Works
1. VAE Compression:
   - The original image is compressed by the VAE into a latent representation.
2. VAE Decompression:
   - The VAE decompresses the latent representation into an image that is highly similar to the original.
3. Image Quality Assessment:
   - Image Quality Assessments are performed on the original image and the new image to aquire three separate accuracy scores that can be used to judge the model's accuracy.

## Acknowledgements
### Images
- VAE Example Image - [VAE Example](https://towardsdatascience.com/stable-diffusion-using-hugging-face-501d8dbdd8)
- VAE Test Image 1 - [Squirrel](https://upload.wikimedia.org/wikipedia/commons/1/1c/Squirrel_posing.jpg)
- VAE Test Image 2 - [Rockefeller Center](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg/798px-View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg)
- VAE Test Image 3 - [Neon](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Neon.JPG/799px-Neon.JPG)
- VAE Test Image 4 - [Starry Night](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/757px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg)
- VAE Test Image 5 - [Alto Saxophone](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Alto_saxophone-E_1685-IMG_7092-gradient.jpg/600px-Alto_saxophone-E_1685-IMG_7092-gradient.jpg)

### Libraries
- OpenCV Library - https://opencv.org
- NumPy Library - https://numpy.org
- Diffusers Library - https://github.com/huggingface/diffusers
- Transformers Library - https://github.com/huggingface/transformers
- FastDownload Library - https://pypi.org/project/fastdownload/
- IO Library - https://www.askpython.com/python-modules/python-io-module
- Pandas Library - https://pandas.pydata.org/docs/getting_started/install.html





