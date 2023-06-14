import pendulum
import pandas as pd
import geopandas as gpd
from shapely import wkb

from .constants import MODEL_DATA_PATH, Y_NAME

def get_timestamp():
    t = pendulum.now(tz='America/Los_Angeles')
    return t.to_iso8601_string()

def _clean_up_gdf(gdf, geometry='geometry'):
    gdf[geometry] = gdf[geometry].apply(wkb.loads)
    gdf = gpd.GeoDataFrame(gdf, geometry=geometry, crs=4326)
    return gdf

def get_model_data(version):
    """Helper for pulling model data off gcs"""
    parts = ['train', 'test']
    tables = ['X', 'y', 'context']
    data_tables = {}
    for part in parts:
        for table in tables:
            data_tables[f'{table}_{part}'] = pd.read_parquet(
                MODEL_DATA_PATH.format(version=version, part=part, table=table))

    X_train = data_tables['X_train']
    X_test = data_tables['X_test']
    y_train = data_tables['y_train'][Y_NAME]
    y_test = data_tables['y_test'][Y_NAME]
    context_train = _clean_up_gdf(data_tables['context_train'], geometry='centroid')
    context_test = _clean_up_gdf(data_tables['context_test'], geometry='centroid')
        
    return X_train, X_test, y_train, y_test, context_train, context_test