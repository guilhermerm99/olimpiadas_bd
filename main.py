from flask import Flask
from routes.pais_routes import pais_bp
from routes.confederacao_routes import conf_bp
from routes.atleta_routes import atleta_bp

app = Flask(__name__)

# Registrando as rotas
app.register_blueprint(pais_bp, url_prefix='/api')
app.register_blueprint(conf_bp, url_prefix='/api')
app.register_blueprint(atleta_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
