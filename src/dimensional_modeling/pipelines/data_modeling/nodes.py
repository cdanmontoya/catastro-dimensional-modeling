"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 0.18.7
"""
import pandas as pd
import numpy as np


def get_dimension_estratos() -> pd.DataFrame:
    d = {
        'id_estrato': [1, 2, 3, 4, 5, 6],
        'estrato': ['Bajo-Bajo', 'Bajo', 'Medio-Bajo', 'Medio', 'Medio-Alto', 'Alto']
    }
    return pd.DataFrame(data=d)


def get_dimension_destinaciones(est_manz: pd.DataFrame) -> pd.DataFrame:
    dimension_destinaciones_df = pd.DataFrame(est_manz.destinacion.unique(), columns=['destinacion']).reset_index().rename(columns={'index': 'id_destinacion'})

    return dimension_destinaciones_df


def get_dimension_ubicacion(est_manz: pd.DataFrame, nom_domc: pd.DataFrame, lote_pred: pd.DataFrame) -> pd.DataFrame:
    nom_domc['comuna'] = nom_domc.comuna.astype('int').astype(str)
    nom_domc['barrio'] = nom_domc.barrio.astype(str)
    lote_pred['id_ubicacion'] = lote_pred.id_ubicacion.astype('int').astype(str)

    dimension_ubicacion_df = est_manz
    dimension_ubicacion_df['comuna'] = dimension_ubicacion_df.barrio.astype('int').astype(str).str[-2:]
    dimension_ubicacion_df['barrio'] = dimension_ubicacion_df.barrio.astype('int').astype(str).str[-2:]
    dimension_ubicacion_df['manzana'] = dimension_ubicacion_df.id_ubicacion.astype('int').astype(str).str[-3:]
    dimension_ubicacion_df.drop_duplicates(inplace=True)
    dimension_ubicacion_df['id_ubicacion'] = dimension_ubicacion_df.id_ubicacion.astype('int').astype(str)

    dimension_ubicacion_df = dimension_ubicacion_df.merge(nom_domc, how='inner',
                                                          on=['comuna', 'barrio'])
    dimension_ubicacion_df = dimension_ubicacion_df.merge(lote_pred, how='inner', on=['id_ubicacion'])
    return dimension_ubicacion_df

def get_hecho_manzanas(aux_estrato: pd.DataFrame, dim_estrato: pd.DataFrame, dim_dest: pd.DataFrame, est_manz: pd.DataFrame) -> pd.DataFrame:
    aux_estrato = (
        aux_estrato.merge(dim_estrato, how='inner', on=['id_estrato']).merge(est_manz, how='inner', on=['id_ubicacion'])
        [['id_ubicacion', 'id_estrato']]
        .drop_duplicates()
        .groupby('id_ubicacion')
        .agg(id_estrato=('id_estrato', pd.Series.median))
        )
    aux_estrato['id_estrato'] = aux_estrato.id_estrato.apply(np.floor).astype(int)
    aux_estrato.reset_index(inplace=True)

    hecho_manzanas_df = (est_manz.merge(dim_dest, how='inner', on=['destinacion']).drop(columns='destinacion')
                         .merge(aux_estrato, how='inner', on=['id_ubicacion']))

    hecho_manzanas_df = hecho_manzanas_df[['id', 'poblacion_aprox', 'cant_predios', 'poblacion_aprox_por_predio', 'id_ubicacion', 'id_destinacion', 'id_estrato']]

    return hecho_manzanas_df

