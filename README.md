# ckd-knn-classifier-bartolia

Starter data science project for predicting chronic kidney disease (CKD) with a K-Nearest Neighbors (KNN) classifier in Python.

## Project structure

- `README.md` – project overview and quick start
- `data/` – place the CKD CSV dataset here (`chronic_kidney_disease.csv`)
- `notebooks/ckd_knn_starter.ipynb` – starter notebook with cleaning, training, evaluation, and plots
- `src/preprocessing.py` – helper functions for loading data, cleaning missing values, and preparing model inputs

## Quick start

1. Create and activate a Python environment.
2. Install required libraries:
   - `pandas`
   - `numpy`
   - `scikit-learn`
   - `matplotlib`
   - `jupyter`
3. Put the dataset file at `data/chronic_kidney_disease.csv`.
4. Open and run `notebooks/ckd_knn_starter.ipynb`.

## Notebook coverage

The starter notebook includes:

- Data loading from CSV
- Data cleaning and missing-value handling
- Training a `KNeighborsClassifier` with `GridSearchCV`
- Performance evaluation with accuracy
- Confusion matrix visualization
- Plot of KNN grid search results
