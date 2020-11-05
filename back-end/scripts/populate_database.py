from repository.db import init_db
from discentes.resource import cadastrar_discente
from disciplinas.resource import cadastrar_disciplina
from config import TestConfig


def popular_discentes():
    cadastrar_discente(1, "Gabriel", "Xará", "gabrielxara@poli.ufrj.br",
                       "cos482", 20, 9, 1996, "Eng. Computação e Informação", 1)
    cadastrar_discente(2, "Lucas", "Chagas", "lucaschagas@poli.ufrj.br",
                       "cos482", 20, 9, 1996, "Eng. Computação e Informação", 1)


def popular_disciplinas():
    cadastrar_disciplina(1, "Qualidade de Software", 4, "COS482", 30, 10, ["Terça", "Quinta"], "")
    cadastrar_disciplina(2, "Gestão da Inovação", 4, "COP232", 30, 13, ["Quarta"], "")
