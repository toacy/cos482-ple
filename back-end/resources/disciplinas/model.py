from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.ext.mutable import MutableList
from repository.db import Base


class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    creditos = Column(Integer, unique=False)
    codigo = Column(String(6), unique=True)
    vagas = Column(Integer, unique=False)
    horario = Column(Integer, unique=False)
    dias = Column(MutableList.as_mutable(PickleType), unique=False)
    requisito = Column(Integer, unique=False)
    inscritos = Column(MutableList.as_mutable(PickleType), unique=False)

    def __init__(self, id, nome, creditos, codigo, vagas, horario, dias, requisito, inscritos):
        self.id = id
        self.nome = nome
        self.creditos = creditos
        self.codigo = codigo
        self.vagas = vagas
        self.horario = horario
        self.dias = dias
        self.requisito = requisito
        self.inscritos = inscritos

    def __repr__(self):
        return '<Disciplina %r>' % (self.nome)