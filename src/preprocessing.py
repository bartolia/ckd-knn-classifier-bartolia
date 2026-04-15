"""Data preparation helpers for the CKD KNN notebook."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


NEGATIVE_LABELS = {"notckd", "not ckd", "0", "no", "negative"}
POSITIVE_LABELS = {"ckd", "1", "yes", "positive"}


def load_dataset(csv_path: Path | str) -> pd.DataFrame:
    """Load CKD CSV data into a DataFrame."""
    return pd.read_csv(csv_path)


def clean_ckd_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize placeholders and impute missing values."""
    cleaned = df.copy()
    cleaned = cleaned.replace("?", np.nan)

    for col in cleaned.select_dtypes(include="object"):
        cleaned[col] = cleaned[col].map(lambda value: value.strip() if isinstance(value, str) else value)

    for col in cleaned.columns:
        cleaned[col] = pd.to_numeric(cleaned[col], errors="ignore")

    numeric_cols = cleaned.select_dtypes(include=np.number).columns
    categorical_cols = cleaned.columns.difference(numeric_cols)

    if len(numeric_cols) > 0:
        cleaned[numeric_cols] = cleaned[numeric_cols].fillna(cleaned[numeric_cols].median())

    for col in categorical_cols:
        mode = cleaned[col].mode()
        fill_value = mode.iloc[0] if not mode.empty else "unknown"
        cleaned[col] = cleaned[col].fillna(fill_value)

    return cleaned


def prepare_features_and_target(df: pd.DataFrame, target_col: str = "classification") -> tuple[pd.DataFrame, pd.Series]:
    """Split a cleaned DataFrame into model features and numeric target labels."""
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in DataFrame")

    target = df[target_col].astype(str).str.strip().str.lower()
    mapping = {label: 0 for label in NEGATIVE_LABELS} | {label: 1 for label in POSITIVE_LABELS}
    y = target.map(mapping)
    if y.isna().any():
        unknown = sorted(target[y.isna()].unique())
        raise ValueError(f"Unsupported target labels: {unknown}")

    X = pd.get_dummies(df.drop(columns=[target_col]), drop_first=True)
    return X, y.astype(int)
