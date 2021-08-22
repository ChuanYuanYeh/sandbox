import os
import argparse
import json
import pandas as pd
import requests


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-files', nargs='+', help='List of JSON files')
    return parser.parse_args()


def main():
    args = setup_args()
    final = pd.DataFrame() 
    for file in args.files:
        df = pd.read_json(os.path.join('data/processed', f'{file}.json'))
        try:
            final = final.merge(df, on='recipe_id')
        except KeyError:
            final = df
    final['date'] = final['date'].astype(str)
    final.rename(
        columns={
            'sample_weight_zn02': 'sample_weight_zno2',
            'color_code': 'color'
        },
        inplace=True
    )
    records = final.to_dict('records')

    for idx, record in enumerate(records):
        print(f'Posting record {idx}')
        r = requests.post(
            url='http://localhost:8000/api/recipes/',
            auth=('cyyeh', '2413'),
            data=record
        )
        print(r.reason)


if __name__ == '__main__':
    main()
