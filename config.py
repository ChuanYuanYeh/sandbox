import os

from pandas.core.base import DataError


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(ROOT_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'to_be_processed')
PROCEESED_DIR = os.path.join(DATA_DIR, 'processed')

REST_API = os.getenv('REST_API')
REST_API_USER = os.getenv('REST_API_USER')
REST_API_PASSWORD = os.getenv('REST_API_PASSWORD')
