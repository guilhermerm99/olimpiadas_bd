from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from models.atleta import Atleta
from database.database import get_db

atleta_bp = Blueprint('atleta', __name__)

# Create
@atleta_bp.route('/atleta', methods=['POST'])
def criar_atleta():
    db: Session = next(get_db())
    data = request.json
    novo_atleta = Atleta(nome=data['nome'], genero=data['genero'], data_nasc=data['data_nasc'],
                         id_confederacao=data['id_confederacao'], id_modalidade=data.get('id_modalidade'))
    db.add(novo_atleta)
    db.commit()
    return jsonify({"message": f"Atleta {data['nome']} criado com sucesso."}), 201

# Read
@atleta_bp.route('/atleta', methods=['GET'])
def listar_atletas():
    db: Session = next(get_db())
    atletas = db.query(Atleta).all()
    return jsonify([{"id": a.id_atleta, "nome": a.nome, "genero": a.genero, "data_nasc": a.data_nasc.isoformat()} for a in atletas]), 200

# Update
@atleta_bp.route('/atleta/<int:id_atleta>', methods=['PUT'])
def atualizar_atleta(id_atleta):
    db: Session = next(get_db())
    atleta = db.query(Atleta).filter_by(id_atleta=id_atleta).first()
    data = request.json
    if atleta:
        atleta.nome = data['nome']
        atleta.genero = data['genero']
        atleta.data_nasc = data['data_nasc']
        atleta.id_confederacao = data['id_confederacao']
        db.commit()
        return jsonify({"message": "Atleta atualizado com sucesso."}), 200
    return jsonify({"message": "Atleta não encontrado."}), 404

# Delete
@atleta_bp.route('/atleta/<int:id_atleta>', methods=['DELETE'])
def deletar_atleta(id_atleta):
    db: Session = next(get_db())
    atleta = db.query(Atleta).filter_by(id_atleta=id_atleta).first()
    if atleta:
        db.delete(atleta)
        db.commit()
        return jsonify({"message": "Atleta excluído com sucesso."}), 200
    return jsonify({"message": "Atleta não encontrado."}), 404
