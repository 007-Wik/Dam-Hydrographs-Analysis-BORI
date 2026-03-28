"""
data_loader.py
Kurnur (BORI) Dam – Breach & Hydrograph Analysis
Reusable data loading and validation functions.

Usage:
    from src.utils.data_loader import load_hydrograph, validate_schema

Author: Satwik Udupi
"""

import pandas as pd
from pathlib import Path

# ── Expected column schemas ────────────────────────────────────────────────────
SCHEMAS = {
    "piping": {
        "required": ["Time", "HW_Elevation_m", "TW_Elevation_m", "Q_Total_m3s", "Q_Breach_m3s"],
        "optional": [],
    },
    "overtopping": {
        "required": ["Time", "HW_Elevation_m", "TW_Elevation_m", "Q_Total_m3s", "Q_Breach_m3s"],
        "optional": [],
    },
    "lcr": {
        "required": ["Time", "HW_Elevation_m", "TW_Elevation_m", "Q_Total_m3s"],
        "optional": [],
    },
    "breach_params": {
        "required": ["Time", "Breach_Width_m", "Breach_Velocity_ms"],
        "optional": ["Breach_Elevation_m"],
    },
}

DATA_DIR = Path(__file__).parents[2] / "data" / "raw"


def load_hydrograph(scenario: str, filepath: str = None, sheet_name: int = 0) -> pd.DataFrame:
    """
    Load a hydrograph Excel file and return a validated DataFrame.

    Parameters
    ----------
    scenario : str
        One of: 'piping', 'overtopping', 'lcr', 'breach_params'
    filepath : str or Path, optional
        Path to Excel file. If None, uses default data/raw/ path.
    sheet_name : int or str
        Sheet index or name (default 0 = first sheet).

    Returns
    -------
    pd.DataFrame
        Loaded and time-indexed DataFrame.
    """
    default_files = {
        "piping":        DATA_DIR / "Piping_Breach_Hydrograph.xlsx",
        "overtopping":   DATA_DIR / "Overtopping_Breach_Hydrograph.xlsx",
        "lcr":           DATA_DIR / "Large_Controlled_Release_Hydrograph.xlsx",
        "breach_params": DATA_DIR / "Overtopping_Piping_Breach_Parameters.xlsx",
    }

    if filepath is None:
        if scenario not in default_files:
            raise ValueError(f"Unknown scenario '{scenario}'. Choose from: {list(default_files)}")
        filepath = default_files[scenario]

    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    df = pd.read_excel(filepath, sheet_name=sheet_name, engine="openpyxl")
    df = df.dropna(how="all")  # drop fully empty rows

    print(f"[load_hydrograph] Loaded '{filepath.name}': {df.shape[0]} rows × {df.shape[1]} cols")
    return df


def validate_schema(df: pd.DataFrame, scenario: str) -> bool:
    """
    Validate that a DataFrame contains the required columns for a scenario.

    Parameters
    ----------
    df : pd.DataFrame
    scenario : str

    Returns
    -------
    bool – True if valid, raises ValueError if not.
    """
    if scenario not in SCHEMAS:
        raise ValueError(f"Unknown scenario: {scenario}")

    required = SCHEMAS[scenario]["required"]
    missing = [col for col in required if col not in df.columns]

    if missing:
        raise ValueError(
            f"Schema validation failed for '{scenario}'. "
            f"Missing columns: {missing}. "
            f"Found: {list(df.columns)}"
        )

    print(f"[validate_schema] Schema OK for '{scenario}'.")
    return True


def extract_peak(df: pd.DataFrame, discharge_col: str, time_col: str = "Time"):
    """
    Extract peak discharge, time-to-peak, and return as dict.

    Returns
    -------
    dict with keys: Q_peak, T_peak, idx_peak
    """
    idx_peak = df[discharge_col].idxmax()
    return {
        "Q_peak":  df.loc[idx_peak, discharge_col],
        "T_peak":  df.loc[idx_peak, time_col],
        "idx_peak": idx_peak,
    }
