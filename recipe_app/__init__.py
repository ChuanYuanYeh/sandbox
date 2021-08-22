"""
    Domain-specific objects are contained here.
"""
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

from utils.dataframe import to_json


def transform_excel(df: DataFrame) -> DataFrame:
    try:
        sample_color_columns = {
            0: 'sample_color_1',
            1: 'sample_color_2',
            2: 'sample_color_3',
            3: 'sample_color_4',
            4: 'sample_color_5',
            5: 'sample_color_6',
        }
        sample_weight_columns = {
            0: 'sample_weight_1',
            1: 'sample_weight_2',
            2: 'sample_weight_3',
            3: 'sample_weight_4',
            4: 'sample_weight_5',
            5: 'sample_weight_6',
        }
        init = pd.pivot_table(df, index=['recipe_id'], values=['color', 'weight_sample', 'weight_production'], aggfunc=lambda x:list(x))
        sample_colors = pd.DataFrame(init['color'].to_list())
        sample_colors.insert(0, 'recipe_id', init.index)
        sample_colors.rename(columns=sample_color_columns, inplace=True)
        for col in sample_color_columns.values():
            if col not in sample_colors:
                sample_colors[col] = None
        sample_colors[[
            'production_color_1',
            'production_color_2',
            'production_color_3',
            'production_color_4',
            'production_color_5',
            'production_color_6',
        ]] = sample_colors[[
            'sample_color_1',
            'sample_color_2',
            'sample_color_3',
            'sample_color_4',
            'sample_color_5',
            'sample_color_6',
        ]]
        sample_colors.fillna('', inplace=True)

        sample_color_weights = pd.DataFrame(init['weight_sample'].to_list())
        sample_color_weights.insert(0, 'recipe_id', init.index)
        sample_color_weights.rename(columns=sample_weight_columns, inplace=True)
        for col in sample_weight_columns.values():
            if col not in sample_color_weights:
                sample_color_weights[col] = np.nan
        sample_color_weights[[
            'production_weight_1',
            'production_weight_2',
            'production_weight_3',
            'production_weight_4',
            'production_weight_5',
            'production_weight_6',
        ]] = sample_color_weights[[
            'sample_weight_1',
            'sample_weight_2',
            'sample_weight_3',
            'sample_weight_4',
            'sample_weight_5',
            'sample_weight_6',
        ]]
        sample_color_weights.fillna(0, inplace=True)

        transformed = pd.merge(sample_colors, sample_color_weights, on='recipe_id')
    except KeyError:
        df.dropna(subset=['recipe_id'], inplace=True)
        df['date'] = df['date'].astype(str)

        transformed = df.fillna('')
    
    return transformed


def transform_json(final: DataFrame) -> dict:
    final['date'] = final['date'].astype(str)
    final.rename(
        columns={
            'sample_weight_zn02': 'sample_weight_zno2',
            'color_code': 'color'
        },
        inplace=True
    )
    records = to_json(final)

    return records
