# Spam Neural Network

## Overview

This project was created as part of an assignment in a Programming II class. The assignment required the creation and training of a boolean neural network using a simple dataset. The goal was to create a neural network that could read the subject line of an email and determine whether the email was "Spam" or "Ham."

- Spam: Unsolicited and often irrelevant or inappropriate messages sent over the internet to a large number of recipients.
- Ham: Legitimate, non-spam emails that are desired and expected by the recipient.

## Features
- Creation and training of a neural network using Scikit-Learn.
- Classification of email subject lines as Spam or Ham.
- Accuracy evaluation of the neural network's predictions.

## Getting Started

### Prerequisites
- Python 3.6 or higher.
- Scikit-Learn library.
- Pandas library.

### Installation
Clone the repository:

git clone https://github.com/qmmartin/Portfolio

Open the project in your preferred IDE.

### Python Scripts
- nn.py: The main script to run the neural network training and testing process.

### How It Works

1. Training the Neural Network:
    - The neural network is trained on the dataset of negative keywords and phrases.
    - Scikit-Learn is used to create and train the neural network.

2. Testing the Neural Network:
    - The trained neural network is tested on a separate dataset of email subject lines, classifying each as Spam or Ham.
    - The network's guesses are compared to the correct classifications to determine accuracy.

3. Accuracy Evaluation:
    - A percentage score of accuracy is printed to the console.
    - The average accuracy is calculated after running the neural network 10 times, with the final average accuracy being 98.52%.

## Acknowledgements
- Sci-kit Learn - https://scikit-learn.org/stable/
- Pandas - https://pandas.pydata.org/docs/getting_started/install.html