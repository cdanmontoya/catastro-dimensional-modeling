"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (clean_estadisticas_por_manzana,
                    clean_nomenclatura_domiciliaria,
                    clean_lote_del_predio,
                    auxiliar_estrato)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=clean_estadisticas_por_manzana,
            inputs=['estadisticas_por_manzana'],
            outputs='clean_estadisticas_por_manzana',
            name='clean_estadisticas_por_manzana'
        ),
        node(
            func=clean_nomenclatura_domiciliaria,
            inputs=['nomenclatura_domiciliaria'],
            outputs='clean_nomenclatura_domiciliaria',
            name='clean_nomenclatura_domiciliaria'
        ),
        node(
            func=clean_lote_del_predio,
            inputs=['lote_del_predio'],
            outputs='clean_lote_del_predio',
            name='clean_lote_del_predio'
        ),
        node(
            func=auxiliar_estrato,
            inputs=['estrato_socioeconomico'],
            outputs='auxiliar_estrato',
            name='auxiliar_estrato'
        )
    ])
