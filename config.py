import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'zoosrv.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacizoo'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'elronia'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Easy1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacityblobstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '9OI4SwaRWX8O5isdajGYmR+PACARjxPNmMAe//WA2Obi9Vbyvdhi+AxyCCVFS6VWNZhoD8Im5atX+9YTnYOO/g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

