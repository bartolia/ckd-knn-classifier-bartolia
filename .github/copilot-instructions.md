# Project Guidelines

## Code Style
- Keep changes small and focused; preserve existing function names and signatures in src/preprocessing.py unless a task explicitly asks for API changes.
- Prefer pandas and scikit-learn idioms already used in this repo (DataFrame transforms, Pipeline, GridSearchCV).
- For notebook edits, keep cells ordered as: imports/setup, data load, cleaning, modeling, evaluation, visualization.

## Architecture
- src/preprocessing.py contains reusable data prep utilities:
  - load_dataset(csv_path)
  - clean_ckd_dataframe(df)
  - prepare_features_and_target(df, target_col='classification')
- notebooks/ckd_knn_starter.ipynb is the end-to-end workflow using those utilities.
- data/ stores datasets; data/raw currently contains the provided source CSV.

## Build and Test
- This repo has no automated test suite or CI configuration.
- Typical setup:
  1. Create and activate a Python environment.
  2. Install dependencies: pandas, numpy, scikit-learn, matplotlib, jupyter.
  3. Run the notebook: jupyter notebook notebooks/ckd_knn_starter.ipynb
- If code changes are made in src/, validate by running the notebook flow end-to-end.

## Conventions and Pitfalls
- Missing values are represented as "?" and should be normalized before modeling.
- prepare_features_and_target defaults to target_col='classification'.
- The current raw dataset at data/raw/Sec001_ckd_dataset_v2.csv uses column names that may differ from notebook expectations (for example class vs classification). Align column names or pass the correct target_col when preparing features.
- README quick-start expects data/chronic_kidney_disease.csv, while the checked-in dataset is under data/raw/. Do not assume the file is already in data/ unless the task sets it up.

## References
- See README.md for project overview and quick start.
- See src/preprocessing.py for canonical cleaning and target-label mapping behavior.
- See notebooks/ckd_knn_starter.ipynb for the baseline KNN workflow and evaluation plots.
