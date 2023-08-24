GCS_PATH = 'gs://smart4'

GROUPER_COL = 'h3_7'
Y_NAME = 'AADB'

# For storing the train/test splits of X/y/context data, when it's ready to dump into skl
MODEL_DATA_PATH = f'{GCS_PATH}/model_data/{{version}}/{{part}}/{{table}}.parquet'

# For storing the results of model runs (model object, accuracy measures, etc.)
MODEL_PATH = f'{GCS_PATH}/models/{{version}}.pkl'

CURRENT_MODEL_DATA_VERSION = '2023-07-15T08:13:02.606521-07:00'