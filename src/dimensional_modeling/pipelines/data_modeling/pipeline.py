"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (get_dimension_estratos,
                    get_dimension_destinaciones,
                    get_dimension_ubicaciones,
                    get_hecho_manzanas)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=get_dimension_estratos,
            inputs=[],
            outputs='dimension_estratos',
            name='get_dimension_estratos'
        ),
        node(
            func=get_dimension_destinaciones,
            inputs=['clean_estadisticas_por_manzana'],
            outputs='dimension_destinaciones',
            name='get_dimension_destinaciones'
        ),
        node(
            func=get_dimension_ubicaciones,
            inputs=['clean_estadisticas_por_manzana', 'clean_nomenclatura_domiciliaria', 'clean_lote_del_predio'],
            outputs='dimension_ubicaciones',
            name='get_dimension_ubicaciones'
        ),
        node(
            func=get_hecho_manzanas,
            inputs=['auxiliar_estrato', 'dimension_estratos', 'dimension_destinaciones',
                    'clean_estadisticas_por_manzana'],
            outputs='hecho_manzanas',
            name='get_hecho_manzanas'
        )
    ])
