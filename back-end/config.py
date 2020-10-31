from os import getenv


class TestConfig:
    DATABASE_URI = 'sqlite:///test_database.sqlite'
    API_ROOT = '/api'
    TESTING = True


class ProductionConfig:
    TESTING = False
    PREFERRED_URL_SCHEME = 'https'
    API_ROOT = '/api'
    API_PORT = getenv('PORT', 8080)
    CONNECTION_NAME = getenv('CONNECTION_NAME')
    DB_PASSWORD = getenv('DB_PASSWORD', 'postgres')
    DB_NAME = getenv('DB_NAME', 'stonelog')
    DB_USER = getenv('DB_USER', 'postgres')
    DB_DRIVER_NAME = 'postgres+pg8000'
    DB_HOST = getenv('DB_HOST')
    DB_QUERY = {'unix_sock': f'/cloudsql/{getenv("CONNECTION_NAME")}/.s.PGSQL.5432'}
