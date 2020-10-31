from sqlalchemy import Column, Integer, String
from repository.db import Base


class User(Base):
    __tablename__ = 'discentes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, nome=None, email=None):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return '<Aluno %r>' % (self.nome)


class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    creditos = Column(Integer, unique=False)
