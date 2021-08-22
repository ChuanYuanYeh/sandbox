"""
    This file contains functions dealing with JSON.
"""
import json
import os
import pathlib

from config import PROCEESED_DIR


def write_json(object: dict, filename: str) -> None:
    pathlib.Path(PROCEESED_DIR).mkdir(parents=True, exist_ok=True)
    outpath = os.path.join(PROCEESED_DIR, f'{filename}.json')
    with open(outpath, 'w') as fp:
        json.dump(object, fp)
