
from flask import Flask
import os
from config import ProductionConfig, TestConfig
from health_check.resource import health_check
from discentes.resource import lista_discentes, cadastrar_discente, alterar_dados_discente, buscar_dados_discente
from repository.db import init_db
from scripts.populate_database import popular_discentes


if os.path.exists('test_database.sqlite'):
    os.remove('test_database.sqlite')


def create_app(config_obj):
    app = Flask(__name__)
    config = config_obj()
    app.config.from_object(config)

    init_db(config)
    popular_discentes()

    app.add_url_rule('/health-check', 'health_check', health_check)
    app.add_url_rule('/discentes', 'lista_discentes', lista_discentes)
    app.add_url_rule('/discentes/<int:id_discente>', 'alterar_dados_discente', alterar_dados_discente, methods=["PUT"])
    app.add_url_rule('/discentes/<int:id_discente>', 'buscar_dados_discente', buscar_dados_discente, methods=["GET"])
    return app


app = create_app(TestConfig)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
