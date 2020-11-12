from flask import jsonify, request
from repository.db import db_session
from resources.disciplinas.model import Disciplina
from resources.discentes.model import Discente


def lista_disciplinas():
    """
    Retorna a lista de disciplinas da universidade
    """
    disciplinas = Disciplina.query.all()
    return jsonify({
        "disciplinas": [
            {
                "id": d.id,
                "nome": d.nome,
                "creditos": d.creditos,
                "codigo": d.codigo,
                "vagas": d.vagas,
                "horario": d.horario,
                "dias": d.dias,
                "requisito": d.requisito,
                "inscritos": d.inscritos
            } for d in disciplinas]
    })


def detalha_disciplina(id_disciplina):
    """
    Retorna as informações cadastradas a respeito de uma disciplina
    """
    infos = Disciplina.query.get(id_disciplina)
    return {
        "id": infos.id,
        "nome": infos.nome,
        "creditos": infos.creditos,
        "codigo": infos.codigo,
        "vagas": infos.vagas,
        "horario": infos.horario,
        "dias": infos.dias,
        "requisito": infos.requisito,
        "inscritos": infos.inscritos
    }


def cadastrar_disciplina(id, nome, creditos, codigo, vagas, horario, dias, requisito):
    u = Disciplina(id, nome, creditos, codigo, vagas, horario, dias, requisito, [])
    db_session.add(u)
    db_session.commit()
    return "Disciplina cadastrada com sucesso"


def inscrever_discente(id_disciplina, id_discente):
    """
    Inscreve um aluno em uma disciplina
    """

    disciplina = Disciplina.query.get(id_disciplina)

    if(disciplina.vagas > 0):
        setattr(disciplina, "inscritos", disciplina.inscritos + [id_discente])
        setattr(disciplina, "vagas", disciplina.vagas-1)
        db_session.commit()

        return "Aluno inscrito com sucesso"
    else:
        verificar_prioridade(id_disciplina, id_discente)

        return


def trancar_inscricao_discente(id_disciplina, id_discente):
    """
    Tranca a inscrição de um aluno que esteja inscrito em uma disciplina
    """
    disciplina = Disciplina.query.get(id_disciplina)

    disciplina.inscritos.remove(id_discente)
    setattr(disciplina, "vagas", disciplina.vagas+1)
    db_session.commit()

    return "Inscrição trancada com sucesso"


def verificar_prioridade(id_disciplina, id_discente):
    """
    Inscreve aluno caso ele possua maior prioridade que os alunos atualmente inscritos
    """
    disciplina = Disciplina.query.get(id_disciplina)
    aluno_menor_prioridade = Discente.query.get(id_discente)
    prioridade_inicial = aluno_menor_prioridade.prioridade

    for aluno in disciplina.inscritos:
        if (aluno.prioridade < aluno_menor_prioridade.prioridade):
            aluno_menor_prioridade = aluno

    if (aluno_menor_prioridade.prioridade != prioridade_inicial):
        disciplina.inscritos.remove(aluno_menor_prioridade.id)
        setattr(disciplina, "inscritos", disciplina.inscritos + [id_discente])
        db_session.commit()

        return "Aluno inscrito com sucesso"

    else:
        return "Não foi possível concluir a inscrição"
