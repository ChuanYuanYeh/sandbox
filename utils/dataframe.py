"""
    This file contains functions dealing with DataFrames.
"""
import os
from typing import Optional
import pandas as pd
from pandas.core.frame import DataFrame

from config import RAW_DIR
from utils.text import to_snake_case

def extract_from_excel(filename: str, sheet_name: str, header: Optional[int] = 0) -> DataFrame:
    full_path = os.path.join(RAW_DIR, filename)
    df = pd.read_excel(full_path, sheet_name=sheet_name, header=header)
    filtered_df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    filtered_df.columns = map(to_snake_case, filtered_df.columns)

    return filtered_df

def to_json(df:DataFrame) -> dict:
    result = df.to_dict('records')
    return result
