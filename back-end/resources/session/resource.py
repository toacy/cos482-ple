from flask import jsonify, request
from repository.db import db_session
from resources.discentes.model import Discente


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
                "curso": d.curso
            } for d in discentes]
    })


def login():
    body = request.get_json()
    user = Discente.query.filter_by(email=body["email"]).first()

    if not user:
        return "Wrong credentials", 401
    elif user.senha == body["password"]:
        return "Logged in", 200
    return "Wrong credentials", 401


def cadastrar_discente(id, nome, sobrenome, email, senha, dia_nascimento, mes_nascimento, ano_nascimento, curso):
    u = Discente(id, nome, sobrenome, email, senha, dia_nascimento, mes_nascimento, ano_nascimento, curso)
    db_session.add(u)
    db_session.commit()
    return "Aluno cadastrado com sucesso"


def alterar_dados_discente(id_discente):
    """
    Atualiza informações de cadastro de um discente
    """

    params = request.args

    discente = Discente.query.get(id_discente)

    for param in params:
        setattr(discente, param, params[param])
        db_session.commit()

    return {
        "id": discente.id,
        "nome": discente.nome,
        "sobrenome": discente.sobrenome,
        "email": discente.email,
        "dia_nascimento": discente.dia_nascimento,
        "mes_nascimento": discente.mes_nascimento,
        "ano_nascimento": discente.ano_nascimento,
        "curso": discente.curso
    }
