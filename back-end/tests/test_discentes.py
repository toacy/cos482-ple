from config import TestConfig
from repository.db import init_db
from scripts.populate_database import popular_discentes, popular_disciplinas
from resources.discentes.model import Discente
import os
if os.path.exists('test_database.sqlite'):
    os.remove('test_database.sqlite')


init_db(TestConfig)
popular_discentes()
popular_disciplinas()


def test_get_user_list():
    users = Discente.query.all()
    assert type(users) == list and len(users) >= 0


def test_login():
    email = "teste@teste"
    user = Discente.query.filter_by(email=email).first()

    assert user.senha == "cos482"
