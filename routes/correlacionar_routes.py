from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from models.pais import Pais
from models.confederacao import Confederacao
from models.atleta import Atleta
from models.modalidade import Modalidade
from database.database import get_db
import base64

correlacionar_bp = Blueprint('correlacionar', __name__)

@correlacionar_bp.route('/correlacionar', methods=['GET'])
def listar_correlacionados():
    db: Session = next(get_db())

    # Consulta para unir Atleta com sua Confederação, o País da Confederação e a Modalidade do Atleta
    resultado = db.query(Atleta, Confederacao, Pais, Modalidade).join(
        Confederacao, Atleta.id_confederacao == Confederacao.id_confederacao
    ).join(
        Pais, Confederacao.id_pais == Pais.id_pais
    ).join(
        Modalidade, Atleta.id_modalidade == Modalidade.id_modalidade
    ).all()

    resposta = []
    for atleta, confederacao, pais, modalidade in resultado:
        # Verificação do tipo de bandeira
        if isinstance(pais.bandeira, bytes):
            bandeira_base64 = base64.b64encode(pais.bandeira).decode('utf-8')
        else:
            # Se não for bytes, trate como um erro ou converta conforme necessário
            bandeira_base64 = pais.bandeira  # ou outra lógica de conversão, se aplicável

        resposta.append({
            "atleta": {
                "id": atleta.id_atleta,
                "nome": atleta.nome,
                "genero": atleta.genero,
                "data_nasc": atleta.data_nasc.isoformat(),
                "modalidade": {
                    "id": modalidade.id_modalidade,
                    "nome": modalidade.nome
                }
            },
            "confederacao": {
                "id": confederacao.id_confederacao,
                "nome": confederacao.nome
            },
            "pais": {
                "id": pais.id_pais,
                "nome": pais.nome,
                "sigla": pais.sigla,
                "bandeira": bandeira_base64 if bandeira_base64 is not None else None
            }
        })

    return jsonify(resposta), 200
