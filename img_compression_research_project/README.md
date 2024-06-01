# Using Stable Diffusion's Variational Autoencoders for Lossy Image Compression.

This project was originally created as a year long research project to be presented at the International Science and Engineering Fair (ISEF) regional competition for the Arkansas School for Mathematics, Sciences, and the Arts.

<img src="images\vae_example.png" width="800">

The ultimate goal of this project is to be able to compress images while maintaining highly similar quality to the original image and avoiding the introduction of artifacts.

RunwayML's Stable Diffusion v1.5 was utilized for the purposes of this project, specifically the lower storage-intensive 'pruned-emaonly' weight.

The scalar used frequently in the code is from [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) and serves as the inverse standard deviation for the latents of the Variational Autoencoder used in Stable Diffusion 1.5.

The paper found within this file presents much more information than is easily shown within a markdown file. Please read the paper for further information on the project.

# Features
- Img2img VAE compression
- PNG compression
- WebP compression
- File size reduction 
- Latent representation

# Credits 
## Images
VAE Example Image - https://towardsdatascience.com/stable-diffusion-using-hugging-face-501d8dbdd8

VAE Test Image 1 - [Squirrel](https://upload.wikimedia.org/wikipedia/commons/1/1c/Squirrel_posing.jpg)

VAE Test Image 2 - [Rockefeller Center](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg/798px-View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg)

VAE Test Image 3 - [Neon](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Neon.JPG/799px-Neon.JPG)

VAE Test Image 4 - [Starry Night](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/757px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg)

VAE Test Image 5 - [Alto Saxophone](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Alto_saxophone-E_1685-IMG_7092-gradient.jpg/600px-Alto_saxophone-E_1685-IMG_7092-gradient.jpg)

## Libraries
OpenCV Library - https://opencv.org

NumPy Library - https://numpy.org

Diffusers Library - https://github.com/huggingface/diffusers

Transformers Library - https://github.com/huggingface/transformers

FastDownload Library - https://pypi.org/project/fastdownload/

IO Library - https://www.askpython.com/python-modules/python-io-module

Pandas Library - https://pandas.pydata.org/docs/getting_started/install.html





