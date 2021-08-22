"""
    Contains functions related to HTTP requests.
"""
import requests

from config import REST_API, REST_API_USER, REST_API_PASSWORD


def post_record(idx: int, record: dict) -> None:
    print(f'Posting record {idx}')
    r = requests.post(
        url=f'{REST_API}',
        auth=(REST_API_USER, REST_API_PASSWORD),
        data=record
    )
    print(r.reason)
