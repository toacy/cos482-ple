
from flask import Flask
from flask_cors import CORS
import os
from config import ProductionConfig, TestConfig
from resources.health_check.resource import health_check
from resources.discentes.resource import lista_discentes, cadastrar_discente, alterar_dados_discente, buscar_dados_discente
from resources.disciplinas.resource import lista_disciplinas, detalha_disciplina, inscrever_discente, trancar_inscricao_discente
from resources.session.resource import login
from repository.db import init_db
from scripts.populate_database import popular_discentes, popular_disciplinas


if os.path.exists('test_database.sqlite'):
    os.remove('test_database.sqlite')


def create_app(config_obj):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    config = config_obj()
    app.config.from_object(config)

    init_db(config)
    popular_discentes()
    popular_disciplinas()
    app.add_url_rule('/health-check', 'health_check', health_check)
    app.add_url_rule('/discentes', 'lista_discentes', lista_discentes)
    app.add_url_rule('/disciplinas', 'lista_disciplinas', lista_disciplinas)
    app.add_url_rule('/discentes/<int:id_discente>', 'alterar_dados_discente', alterar_dados_discente, methods=["PUT"])
    app.add_url_rule('/authenticate', 'login', login, methods=["POST"])
    app.add_url_rule('/discentes/<int:id_discente>', 'buscar_dados_discente', buscar_dados_discente, methods=["GET"])
    app.add_url_rule('/disciplinas/<int:id_disciplina>', 'detalha_disciplina', detalha_disciplina, methods=["GET"])
    return app


app = create_app(TestConfig)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
