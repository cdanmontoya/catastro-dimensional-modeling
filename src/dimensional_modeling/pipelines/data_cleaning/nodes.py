"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.18.7
"""
import numpy as np
import pandas as pd


def clean_estadisticas_por_manzana(est_manz: pd.DataFrame) -> pd.DataFrame:
    est_manz_df = (
        est_manz[['CANT_PREDIOS', 'POBLACION_APROX', 'OBJECTID', 'COBAMA', 'DESTINACION', 'COMUNA', 'BARRIO']]
        .rename(columns={
            'CANT_PREDIOS': 'cant_predios',
            'POBLACION_APROX': 'poblacion_aprox',
            'OBJECTID': 'id',
            'COBAMA': 'id_ubicacion',
            'DESTINACION': 'destinacion',
            'COMUNA': 'comuna',
            'BARRIO': 'barrio'
        }))

    est_manz_df = est_manz_df[est_manz_df['barrio'].notna()]
    est_manz_df = est_manz_df[est_manz_df['comuna'].notna()]

    est_manz_df['poblacion_aprox_por_predio'] = est_manz_df.poblacion_aprox / est_manz_df.cant_predios
    est_manz_df['poblacion_aprox_por_predio'] = est_manz_df['poblacion_aprox_por_predio'].apply(np.round)

    return est_manz_df


def clean_nomenclatura_domiciliaria(nom_domi: pd.DataFrame) -> pd.DataFrame:
    rename_cols = {
        'CODIGO_BARRIO': 'barrio',
        'NOMBRE_BARRIO': 'nombre_barrio',
        'CODIGO_COMUNA': 'comuna',
        'NOMBRE_COMUNA': 'nombre_comuna'
    }

    nomenclatura_domiciliaria_df = (nom_domi[['CODIGO_BARRIO', 'NOMBRE_BARRIO', 'CODIGO_COMUNA', 'NOMBRE_COMUNA']]
                                    .drop_duplicates()
                                    .rename(columns=rename_cols))

    nomenclatura_domiciliaria_df['barrio'] = nomenclatura_domiciliaria_df.barrio.astype(str).str[-2:]

    return nomenclatura_domiciliaria_df


def clean_lote_del_predio(lote_predio: pd.DataFrame) -> pd.DataFrame:
    lote_del_predio_df_raw = lote_predio[lote_predio['COBAMA'].notna()]
    lote_del_predio_df_raw['id_ubicacion'] = lote_del_predio_df_raw.COBAMA.astype(str).str.split('.').str[0].astype(str)
    lote_del_predio_df = (lote_del_predio_df_raw
                          .groupby('id_ubicacion', as_index=False)
                          .first()
                          .rename(columns={'LONGITUD': 'longitud', 'LATITUD': 'latitud'})
                          [['id_ubicacion', 'latitud', 'longitud']])

    return lote_del_predio_df


def auxiliar_estrato(estrato_socioecono: pd.DataFrame) -> pd.DataFrame:
    auxiliar_estrato_df = estrato_socioecono
    auxiliar_estrato_df['id_ubicacion'] = (auxiliar_estrato_df.MANZANA
                                           .fillna(auxiliar_estrato_df.CODIGO_BARRIO)
                                           .astype(str)
                                           .str.split('.')
                                           .str[0])

    auxiliar_estrato_df = auxiliar_estrato_df.rename(
        columns={'BARRIO': 'barrio', 'COMUNA': 'comuna', 'ESTRATO': 'id_estrato'})
    auxiliar_estrato_df['manzana'] = auxiliar_estrato_df.MANZANA.astype(str).str[4::].str.split('.').str[0]
    auxiliar_estrato_df['barrio'] = auxiliar_estrato_df.barrio.astype(str).str.zfill(2)
    auxiliar_estrato_df = auxiliar_estrato_df[['id_ubicacion', 'comuna', 'barrio', 'manzana', 'id_estrato']]

    return auxiliar_estrato_df
