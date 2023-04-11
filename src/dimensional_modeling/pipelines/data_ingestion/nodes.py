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
