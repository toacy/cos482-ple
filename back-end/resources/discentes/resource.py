from flask import jsonify, request
from repository.db import db_session
from resources.discentes.model import Discente
from services.camunda_service import CamundaService
from config import TestConfig


def lista_discentes():
    """
    Retorna a lista de discentes da universidade
    """
    discentes = Discente.query.all()
    return jsonify({
        "discentes": [
            {
                "id": d.id,
                "nome": d.nome,
                "sobrenome": d.sobrenome,
                "email": d.email,
                "dia_nascimento": d.dia_nascimento,
                "mes_nascimento": d.mes_nascimento,
                "ano_nascimento": d.ano_nascimento,
                "curso": d.curso,
                "prioridade": d.prioridade
            } for d in discentes]
    })


def buscar_dados_discente(id_discente):
    """
    Retorna as informações cadastradas a respeito de um único discente
    """
    infos = Discente.query.get(id_discente)
    return {
        "id": infos.id,
        "nome": infos.nome,
        "sobrenome": infos.sobrenome,
        "email": infos.email,
        "dia_nascimento": infos.dia_nascimento,
        "mes_nascimento": infos.mes_nascimento,
        "ano_nascimento": infos.ano_nascimento,
        "curso": infos.curso,
        "prioridade": infos.prioridade
    }


def cadastrar_discente(id, nome, sobrenome, email, senha, dia_nascimento, mes_nascimento, ano_nascimento, curso, prioridade):
    u = Discente(id, nome, sobrenome, email, senha, dia_nascimento, mes_nascimento, ano_nascimento, curso, prioridade)
    db_session.add(u)
    db_session.commit()
    return "Aluno cadastrado com sucesso"


def alterar_dados_discente(id_discente):
    """
    Atualiza informações de cadastro de um discente
    """

    params = request.args

    camunda_handler = CamundaService("alterar_dados_usuario", config=TestConfig)
    process_data = camunda_handler.start_process()

    camunda_handler.claim_task(process_data["processInstanceId"])
    camunda_handler.complete_task(process_data["processInstanceId"])

    discente = Discente.query.get(id_discente)

    for param in params:
        setattr(discente, param, params[param])
        db_session.commit()

    camunda_handler.claim_task(process_data["processInstanceId"])
    camunda_handler.complete_task(process_data["processInstanceId"])

    return {
        "id": discente.id,
        "nome": discente.nome,
        "sobrenome": discente.sobrenome,
        "email": discente.email,
        "dia_nascimento": discente.dia_nascimento,
        "mes_nascimento": discente.mes_nascimento,
        "ano_nascimento": discente.ano_nascimento,
        "curso": discente.curso,
        "prioridade": discente.prioridade
    }


def detalha_discente(id_discente):
    """
    Informa os dados de cadastro de um discente
    """
    return
