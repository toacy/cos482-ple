from os import getenv


class TestConfig:
    DATABASE_URI = 'sqlite:///test_database.sqlite'
    TESTING = True
    CAMUNDA_SERVER = 'http://localhost:8080/engine-rest'
    CAMUNDA_USER = 'sistema'
    TEST_USER = 'teste@teste'
    TEST_PASS = 'cos482'


class ProductionConfig:
    TESTING = False
    API_PORT = getenv('PORT', 8080)
    CONNECTION_NAME = getenv('CONNECTION_NAME')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DB_NAME = getenv('DB_NAME')
    DB_USER = getenv('DB_USER')
    DB_DRIVER_NAME = 'postgres+psycopg2'
    DB_HOST = getenv('DB_HOST')
    DB_QUERY = {'unix_sock': f'/cloudsql/{getenv("CONNECTION_NAME")}/.s.PGSQL.5432'}
