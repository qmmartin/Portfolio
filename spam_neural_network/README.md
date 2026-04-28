# Spam Neural Network

This project trains and evaluates a binary classifier that labels email subject lines as spam or ham.

## Overview

Originally developed for a Programming II assignment, this project applies supervised learning with scikit-learn to a lightweight email subject dataset.

The model is trained on known scam words and phrases, then evaluated on held-out examples. Across repeated runs, the reported average accuracy was 98.52%.

## Technical Highlights

- Binary text classification pipeline for spam vs ham.
- Dataset preparation with pandas.
- Model training and prediction via scikit-learn.
- Repeated evaluation runs to estimate average performance stability.

## Project Structure

- nn.py: Main training and evaluation script.
- spam.csv: Dataset used for model input and labels.
- Scam Words/Scam_Words.csv: Supporting keyword dataset.

## Requirements

- Python 3.6+
- pandas
- scikit-learn

Install dependencies:

```bash
python -m pip install pandas scikit-learn
```

## Usage

1. Open the spam_neural_network folder.
2. Run nn.py.
3. Review console output for predictions and aggregate accuracy.

## Method

1. Load labeled training data and supporting spam keyword data.
2. Train a binary classifier using scikit-learn.
3. Evaluate predictions on test examples and compute accuracy.
4. Repeat multiple runs to estimate average model performance.

## Future Plans

- Expand the dataset with more diverse and recent subject lines.
- Compare multiple model families and feature extraction strategies.
- Add precision/recall/F1 reporting alongside overall accuracy.

## Resources

- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/docs/getting_started/install.html)