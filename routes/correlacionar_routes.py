from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from models.pais import Pais
from models.confederacao import Confederacao
from models.atleta import Atleta
from database import get_db

correlacionar_bp = Blueprint('correlacionar', __name__)

@correlacionar_bp.route('/correlacionar', methods=['GET'])
def listar_correlacionados():
    db: Session = next(get_db())

    # Consulta para unir Atleta com sua Confederação e o País da Confederação
    resultado = db.query(Atleta, Confederacao, Pais).join(
        Confederacao, Atleta.id_confederacao == Confederacao.id_confederacao
    ).join(
        Pais, Confederacao.id_pais == Pais.id_pais
    ).all()

    # Formatar o resultado em JSON
    resposta = []
    for atleta, confederacao, pais in resultado:
        resposta.append({
            "atleta": {
                "id": atleta.id_atleta,
                "nome": atleta.nome,
                "genero": atleta.genero,
                "data_nasc": atleta.data_nasc.isoformat()
            },
            "confederacao": {
                "id": confederacao.id_confederacao,
                "nome": confederacao.nome
            },
            "pais": {
                "id": pais.id_pais,
                "nome": pais.nome,
                "sigla": pais.sigla
            }
        })

    return jsonify(resposta), 200
