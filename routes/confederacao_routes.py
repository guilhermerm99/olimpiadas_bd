from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from models.confederacao import Confederacao
from database.database import get_db

conf_bp = Blueprint('confederacao', __name__)

# Create
@conf_bp.route('/confederacao', methods=['POST'])
def criar_confederacao():
    db: Session = next(get_db())
    data = request.json
    nova_conf = Confederacao(nome=data['nome'], id_pais=data['id_pais'])
    db.add(nova_conf)
    db.commit()
    return jsonify({"message": f"Confederação {data['nome']} criada com sucesso."}), 201

# Read
@conf_bp.route('/confederacao', methods=['GET'])
def listar_confederacoes():
    db: Session = next(get_db())
    confs = db.query(Confederacao).all()
    return jsonify([{"id": c.id_confederacao, "nome": c.nome, "id_pais": c.id_pais} for c in confs]), 200

# Update
@conf_bp.route('/confederacao/<int:id_conf>', methods=['PUT'])
def atualizar_confederacao(id_conf):
    db: Session = next(get_db())
    conf = db.query(Confederacao).filter_by(id_confederacao=id_conf).first()
    data = request.json
    if conf:
        conf.nome = data['nome']
        conf.id_pais = data['id_pais']
        db.commit()
        return jsonify({"message": "Confederação atualizada com sucesso."}), 200
    return jsonify({"message": "Confederação não encontrada."}), 404

# Delete
@conf_bp.route('/confederacao/<int:id_conf>', methods=['DELETE'])
def deletar_confederacao(id_conf):
    db: Session = next(get_db())
    conf = db.query(Confederacao).filter_by(id_confederacao=id_conf).first()
    if conf:
        db.delete(conf)
        db.commit()
        return jsonify({"message": "Confederação excluída com sucesso."}), 200
    return jsonify({"message": "Confederação não encontrada."}), 404
