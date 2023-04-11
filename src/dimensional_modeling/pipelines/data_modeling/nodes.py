"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 0.18.7
"""
import pandas as pd


def get_dimension_estratos() -> pd.DataFrame:
    d = {
        'id_estrato': [1, 2, 3, 4, 5, 6],
        'estrato': ['Bajo-Bajo', 'Bajo', 'Medio-Bajo', 'Medio', 'Medio-Alto', 'Alto']
    }
    return pd.DataFrame(data=d)
