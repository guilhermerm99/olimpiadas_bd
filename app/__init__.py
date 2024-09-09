from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar e registrar rotas
    from app.routes import (
        listar_atletas, criar_atleta, editar_atleta, deletar_atleta,
        listar_paises, criar_pais, editar_pais, deletar_pais,
        listar_confederacoes, criar_confederacao, editar_confederacao, deletar_confederacao
    )
    
    app.add_url_rule('/atletas', view_func=listar_atletas)
    app.add_url_rule('/atleta/criar', view_func=criar_atleta, methods=['GET', 'POST'])
    app.add_url_rule('/atleta/editar/<int:id>', view_func=editar_atleta, methods=['GET', 'POST'])
    app.add_url_rule('/atleta/deletar/<int:id>', view_func=deletar_atleta, methods=['POST'])

    app.add_url_rule('/paises', view_func=listar_paises)
    app.add_url_rule('/pais/criar', view_func=criar_pais, methods=['GET', 'POST'])
    app.add_url_rule('/pais/editar/<int:id>', view_func=editar_pais, methods=['GET', 'POST'])
    app.add_url_rule('/pais/deletar/<int:id>', view_func=deletar_pais, methods=['POST'])

    app.add_url_rule('/confederacoes', view_func=listar_confederacoes)
    app.add_url_rule('/confederacao/criar', view_func=criar_confederacao, methods=['GET', 'POST'])
    app.add_url_rule('/confederacao/editar/<int:id>', view_func=editar_confederacao, methods=['GET', 'POST'])
    app.add_url_rule('/confederacao/deletar/<int:id>', view_func=deletar_confederacao, methods=['POST'])

    return app
