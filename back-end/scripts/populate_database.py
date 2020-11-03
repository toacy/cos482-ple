from repository.db import init_db
from discentes.resource import cadastrar_discente
from config import TestConfig


def popular_discentes():
    cadastrar_discente(1, "Gabriel", "Xará", "gabrielxara@poli.ufrj.br", 20, 9, 1996, "Eng. Computação e Informação")
    cadastrar_discente(2, "Lucas", "Chagas", "lucaschagas@poli.ufrj.br", 20, 9, 1996, "Eng. Computação e Informação")


def popular_disciplinas():
    return
