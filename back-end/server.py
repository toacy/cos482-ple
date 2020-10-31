
from flask import Flask

from config import ProductionConfig, TestConfig
from health_check.resource import health_check
from repository.db import init_db


def create_app(config_obj):
    app = Flask(__name__)
    config = config_obj()
    app.config.from_object(config)

    init_db(config)

    app.add_url_rule('/health-check', view_func=health_check, methods=['GET'])
    # app.add_url_rule(f'{app.config["API_ROOT"]}/polos', view_func=lista_polos, methods=['GET'])
    # app.add_url_rule(f'{app.config["API_ROOT"]}/polos/<uuid:id_polo>', view_func=detalha_polo, methods=['GET'])
    # app.add_url_rule(f'{app.config["API_ROOT"]}/polos/<uuid:id_polo>/expedicao', view_func=expede_aparelhos,
    #                  methods=['POST'])
    return app


app = create_app(TestConfig)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
