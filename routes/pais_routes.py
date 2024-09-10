from flask import Blueprint, request, jsonify, send_file  # Flask-related imports
from PIL import Image  # Importing Image class from PIL
from io import BytesIO  # For handling byte streams
from sqlalchemy.orm import Session  # SQLAlchemy session management
from database.database import get_db  # Your database session management
from models.pais import Pais  # Direct import of the Pais model

pais_bp = Blueprint('pais_bp', __name__)

@pais_bp.route('/pais', methods=['POST'])
def criar_pais():
    db: Session = next(get_db())
    
    # Verifica se os dados obrigatórios foram enviados
    if 'nome' not in request.form or 'sigla' not in request.form:
        return jsonify({"message": "Campos 'nome' e 'sigla' são obrigatórios."}), 400
    
    data = request.form
    arquivo_bandeira = request.files.get('bandeira')
    bandeira = None
    
    if arquivo_bandeira:
        # Abre e processa o arquivo de imagem
        imagem = Image.open(arquivo_bandeira)
        imagem.thumbnail((400, 400))  # Redimensiona a imagem
        buffer = BytesIO()
        imagem.save(buffer, format="PNG")  # Salva a imagem em formato PNG
        bandeira = buffer.getvalue()  # Obtém o conteúdo da imagem como bytes
    
    novo_pais = Pais(nome=data['nome'], sigla=data['sigla'], bandeira=bandeira)
    db.add(novo_pais)
    db.commit()

    return jsonify({"message": f"País {data['nome']} criado com sucesso."}), 201


@pais_bp.route('/pais', methods=['GET'])
def listar_paises():
    db: Session = next(get_db())
    paises = db.query(Pais).all()
    return jsonify([{
        "id": p.id_pais,
        "nome": p.nome,
        "sigla": p.sigla,
        "bandeira_url": f"/api/pais/{p.id_pais}/bandeira"  # URL para obter a bandeira
    } for p in paises]), 200

@pais_bp.route('/pais/<int:id_pais>', methods=['PUT'])
def atualizar_pais(id_pais):
    db: Session = next(get_db())
    pais = db.query(Pais).filter_by(id_pais=id_pais).first()
    if not pais:
        return jsonify({"message": "País não encontrado."}), 404
    
    # Dados do formulário
    nome = request.form.get('nome')
    sigla = request.form.get('sigla')

    # Arquivo da bandeira
    arquivo_bandeira = request.files.get('bandeira')
    if arquivo_bandeira:
        imagem = Image.open(arquivo_bandeira)
        imagem.thumbnail((400, 400))
        buffer = BytesIO()
        imagem.save(buffer, format="PNG")
        pais.bandeira = buffer.getvalue()
    
    # Atualizando os campos
    if nome:
        pais.nome = nome
    if sigla:
        pais.sigla = sigla

    db.commit()
    return jsonify({"message": "País atualizado com sucesso."}), 200

@pais_bp.route('/pais/<int:id_pais>', methods=['DELETE'])
def deletar_pais(id_pais):
    db: Session = next(get_db())
    pais = db.query(Pais).filter_by(id_pais=id_pais).first()
    if pais:
        db.delete(pais)
        db.commit()
        return jsonify({"message": "País excluído com sucesso."}), 200
    return jsonify({"message": "País não encontrado."}), 404

@pais_bp.route('/pais/<int:id_pais>/bandeira', methods=['GET'])
def obter_bandeira(id_pais):
    db: Session = next(get_db())
    pais = db.query(Pais).filter_by(id_pais=id_pais).first()
    if pais and pais.bandeira:
        return send_file(BytesIO(pais.bandeira), mimetype='image/png')  # Adjust the MIME type if needed
    return jsonify({"message": "Bandeira não encontrada."}), 404
