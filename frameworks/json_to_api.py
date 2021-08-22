import os
import argparse
from typing import Callable, Optional
import pandas as pd
from pandas.core.frame import DataFrame
import requests

from config import PROCEESED_DIR
from utils.dataframe import to_json
from utils.api import post_record


def flow(files: list[str], merge_on: Optional[str], custom_func: Optional[Callable[[DataFrame], dict]] = lambda df: to_json(df)) -> None:
    final = pd.DataFrame()

    for file in files:
        filepath = os.path.join(PROCEESED_DIR, f'{file}.json')
        df = pd.read_json(filepath)
        try:
            final = final.merge(df, on=merge_on or '')
        except KeyError:
            final = df

    records = custom_func(final)

    for idx, record in enumerate(records):
        post_record(idx, record)
