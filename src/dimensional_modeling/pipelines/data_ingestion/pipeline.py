"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import read_estadisticas_por_manzana_response


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=read_estadisticas_por_manzana_response,
            inputs=['estadisticas_por_manzana_api'],
            outputs='estadisticas_por_manzana',
            name='read_estadisticas_por_manzana_response'
        ),
    ])
