import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging
from config import TestConfig


def create_engine_from_config(config):
    logging.info(f'Configurando API. Ambiente de {"TESTE" if config.TESTING else "PRODUÇÃO"}')
    if config.TESTING:
        return create_engine(config.DATABASE_URI)
    return create_engine(
        sqlalchemy.engine.url.URL(
            drivername=config.DB_DRIVER_NAME,
            username=config.DB_USER,
            host=config.DB_HOST,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            query=config.DB_QUERY if config.CONNECTION_NAME else None
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800)


engine = create_engine_from_config(TestConfig)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db(config):
    import discentes.model
    Base.metadata.create_all(bind=engine)
