from sqlalchemy import Column, Integer, String
from repository.db import Base


class Discente(Base):
    __tablename__ = 'discentes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    sobrenome = Column(String(50))
    email = Column(String(120), unique=True)
    senha = Column(String(120))
    dia_nascimento = Column(Integer)
    mes_nascimento = Column(Integer)
    ano_nascimento = Column(Integer)
    curso = Column(String(100))
    prioridade = Column(Integer)

    def __init__(self, id, nome, sobrenome, email, senha, dia_nascimento, mes_nascimento, ano_nascimento, curso, prioridade):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.dia_nascimento = dia_nascimento
        self.mes_nascimento = mes_nascimento
        self.ano_nascimento = ano_nascimento
        self.curso = curso
        self.prioridade = prioridade

    def __repr__(self):
        return '<Aluno %r>' % (self.nome)