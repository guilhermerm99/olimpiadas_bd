from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from models.atleta import Atleta
from database.database import get_db

atleta_bp = Blueprint('atleta', __name__)

@atleta_bp.route('/atleta', methods=['POST'])
def criar_atleta():
    db: Session = next(get_db())
    data = request.json
    if not data:
        return jsonify({"message": "Dados inválidos."}), 400
    
    novo_atleta = Atleta(
        nome=data['nome'],
        genero=data['genero'],
        data_nasc=data['data_nasc'],
        id_confederacao=data['id_confederacao'],
        id_modalidade=data.get('id_modalidade')
    )
    db.add(novo_atleta)
    db.commit()
    return jsonify({"message": f"Atleta {data['nome']} criado com sucesso."}), 201



@atleta_bp.route('/atleta', methods=['GET'])
def listar_atletas():
    db: Session = next(get_db())
    atletas = db.query(Atleta).all()
    return jsonify([{
        "id": a.id_atleta,
        "nome": a.nome,
        "genero": a.genero,
        "data_nasc": a.data_nasc.isoformat()
    } for a in atletas]), 200

@atleta_bp.route('/atleta/<int:id_atleta>', methods=['PUT'])
def atualizar_atleta(id_atleta):
    db: Session = next(get_db())
    atleta = db.query(Atleta).filter_by(id_atleta=id_atleta).first()
    if not atleta:
        return jsonify({"message": "Atleta não encontrado."}), 404

    data = request.json
    atleta.nome = data.get('nome', atleta.nome)
    atleta.genero = data.get('genero', atleta.genero)
    atleta.data_nasc = data.get('data_nasc', atleta.data_nasc)
    atleta.id_confederacao = data.get('id_confederacao', atleta.id_confederacao)
    atleta.id_modalidade = data.get('id_modalidade', atleta.id_modalidade)  # Atualiza também o campo opcional

    db.commit()
    return jsonify({"message": "Atleta atualizado com sucesso."}), 200


@atleta_bp.route('/atleta/<int:id_atleta>', methods=['DELETE'])
def deletar_atleta(id_atleta):
    db: Session = next(get_db())
    atleta = db.query(Atleta).filter_by(id_atleta=id_atleta).first()
    if not atleta:
        return jsonify({"message": "Atleta não encontrado."}), 404

    db.delete(atleta)
    db.commit()
    return jsonify({"message": "Atleta excluído com sucesso."}), 200
