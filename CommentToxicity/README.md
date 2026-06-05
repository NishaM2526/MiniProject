# Comment Toxicity Classification

## Overview

Comment Toxicity is a project that implements text classification models to detect toxic or abusive comments. The repository contains notebooks and scripts for preprocessing, model development (RNN, LSTM, BiLSTM), training, and evaluating models on provided datasets.

## Features
- Data preprocessing pipelines for comment text
- Models: Simple RNN, LSTM, BiLSTM
- Training and evaluation notebooks with metrics reports
- Saved model checkpoints for quick inference

## Repository structure

- Ananlysis/: metric reports and architecture notes
- App/: runnable application CommentToxicity.py
- Code/: model training and preprocessing notebooks
- Data/: datasets used for training and testing
- Model/: saved model checkpoints

## Setup

1. Create and activate a Python virtual environment (recommended):

   python -m venv .venv
   .venv\\Scripts\\activate    # Windows PowerShell

2. Install required packages (example):

   pip install -r requirements.txt

If `requirements.txt` is not present, install core packages used in notebooks: numpy, pandas, scikit-learn, torch, tensorflow (if applicable), nltk.

## Usage

- Preprocess data: open `Code/PreProcessing.ipynb` or `Code/PreProcessingNotebook.ipynb` and run cells to generate cleaned datasets in `Data/`.
- Train a model: open the appropriate notebook in `Code/` (e.g. `BiLSTM_ModelDevelopment.ipynb`) and run training cells. Trained models are saved to `Model/`.
- Run inference / demo: use `App/CommentToxicity.py` to load a model and classify text inputs.

## Evaluation

Metric reports for different architectures are available in Ananlysis/ (e.g. BiLSTM_Metrix_Report.txt). Use these to compare precision, recall, F1-score, and confusion matrices.

## Notes

- Some filenames contain legacy typos (e.g., Ananlysis). Paths listed above match the current workspace structure.
- If you want, I can generate a `requirements.txt` from the environment or add example inference scripts.

## Tech Stack
- Python
- TensorFlow
- Keras
- NLTK
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## Author
Nisha M
