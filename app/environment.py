import os

def get_sqlalchemy_db_uri():
    return 'mysql+pymysql://{0}:{1}@{2}:3308/{3}'.format(  # noqa: E501
        os.environ.get('DB_USERNAME', ''),
        os.environ.get('DB_PASSWORD', ''),
        os.environ.get('DB_HOST', ''),
        os.environ.get('DB_SCHEMA', '')
    )
