import argparse

from frameworks.excel_to_json import flow as  extract_transform
from frameworks.json_to_api import flow as load
from recipe_app import transform_excel, transform_json


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help='Excel filename', const=None)
    parser.add_argument('-sheets', nargs='+', help='List of sheet names to convert')
    return parser.parse_args()


def main():
    args = setup_args()
    extract_transform(filename=args.file, sheets=args.sheets, custom_func=transform_excel)
    load(files=args.sheets, custom_func=transform_json)


if __name__ == '__main__':
    main()
