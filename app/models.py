from app import db

# Modelo Atleta
class Atleta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    id_confederacao = db.Column(db.Integer, nullable=True)
    id_modalidade = db.Column(db.Integer, nullable=True)

# Modelo Evento
class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    local = db.Column(db.String(100), nullable=False)

# Modelo Medalha
class Medalha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    atleta_id = db.Column(db.Integer, db.ForeignKey('atleta.id'), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)

    atleta = db.relationship('Atleta', backref=db.backref('medalhas', lazy=True))
    evento = db.relationship('Evento', backref=db.backref('medalhas', lazy=True))
