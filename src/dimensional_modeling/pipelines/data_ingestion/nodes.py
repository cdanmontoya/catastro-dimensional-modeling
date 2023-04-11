"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.18.7
"""
import pandas as pd

from requests.models import Response


def read_estadisticas_por_manzana_response(response: Response) -> pd.DataFrame:
    data = response.content.decode('utf-8').split('\n')
    data = list(map(lambda x: x.split(','), data))

    return pd.DataFrame(data[1:], columns=data[0])


def read_nomenclatura_domiciliaria_file() -> pd.DataFrame:
    df = pd.read_csv('data/00_ingestion/nomenclatura_domiciliaria.csv', low_memory=False)

    return df


def read_lote_del_predio_file() -> pd.DataFrame:
    df = pd.read_csv('data/00_ingestion/lote_del_predio.csv', low_memory=False)

    return df


def read_estrato_socioeconomico_response(response: Response) -> pd.DataFrame:
    data = response.content.decode('utf-8').split('\n')
    data = list(map(lambda x: x.split(','), data))

    return pd.DataFrame(data[1:], columns=data[0])
