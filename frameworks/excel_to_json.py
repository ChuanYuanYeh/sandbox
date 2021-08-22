"""
    This framework is used to extract and transform Excel files into JSON files.
"""


from typing import Callable, Optional

from pandas.core.frame import DataFrame

from utils.dataframe import extract_from_excel, to_json
from utils.json import write_json


def flow(filename: str, sheets: list[str], custom_func: Optional[Callable[[DataFrame], DataFrame]] = lambda df: df) -> None:
    for sheet in sheets:
        df = extract_from_excel(f'{filename}.xlsx', sheet_name=sheet)
        transformed_df = custom_func(df)
        result = to_json(transformed_df)
        write_json(result, sheet)
