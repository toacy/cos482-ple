import logging
import json
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date,
    ForeignKey, DateTime
)
from sqlalchemy.orm import mapper, relationship
from sqlalchemy_utils import UUIDType
import uuid

from polo.model import Polo, Expedicao, OrdemDeServico

metadata = MetaData()

polos = Table(
    'polos', metadata,
    Column('id_polo', UUIDType, primary_key=True),
    Column('nome', String(64), nullable=False),
    Column('cobertura', Integer, nullable=True)
)

expedicoes = Table(
    'Expedicoes', metadata,
    Column('id', Integer, primary_key=True, a utoincrement=True),
    Column('id_polo', ForeignKey('polos.id_polo')),
    Column('num_terminais', Integer, nullable=False),
    Column('data_expedicao', DateTime, nullable=False)
)

ordens_de_servico = Table(
    'Ordens_de_servico', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_polo', ForeignKey('polos.id_polo')),
    Column('data_atendimento', DateTime, nullable=False)
)


def start_mappers():
    mapper_ordens_de_servico = mapper(OrdemDeServico, ordens_de_servico)
    mapper_expedicoes = mapper(Expedicao, expedicoes)
    mapper(Polo, polos, properties={
        '_terminais_recebidos': relationship(mapper_expedicoes),
        '_ordens_executadas': relationship(mapper_ordens_de_servico)
    })
