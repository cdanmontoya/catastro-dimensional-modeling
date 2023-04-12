"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (read_estadisticas_por_manzana_response,
                    read_nomenclatura_domiciliaria_file,
                    read_lote_del_predio_file,
                    read_estrato_socioeconomico_response)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=read_estadisticas_por_manzana_response,
            inputs=['estadisticas_por_manzana_api'],
            outputs='estadisticas_por_manzana',
            name='read_estadisticas_por_manzana_response'
        ),
        node(
            func=read_nomenclatura_domiciliaria_file,
            inputs=[],
            outputs='nomenclatura_domiciliaria',
            name='read_nomenclatura_domiciliaria_file'
        ),
        node(
            func=read_lote_del_predio_file,
            inputs=[],
            outputs='lote_del_predio',
            name='read_lote_del_predio_file'
        ),
        node(
            func=read_estrato_socioeconomico_response,
            inputs=['estrato_socioeconomico_api'],
            outputs='estrato_socioeconomico',
            name='read_estrato_socioeconomico_response'
        )
    ])
