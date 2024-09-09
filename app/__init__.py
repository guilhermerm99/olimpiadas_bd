# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # Importar as configurações da aplicação

# Inicializa as extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Cria a instância do Flask
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config.from_object(Config)
    
    # Inicializa as extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Importa e registra as rotas
    from . import routes
    app.register_blueprint(routes.bp)
    
    # Aqui, você pode adicionar outras inicializações, como autenticação, se necessário
    
    return app
