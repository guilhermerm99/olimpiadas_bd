from app import db

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    atletas = db.relationship('Atleta', backref='pais', lazy=True)

class Confederacao(db.Model):
    __tablename__ = 'Confederacao'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

class Atleta(db.Model):
    __tablename__ = 'Atleta'
    
    id_atleta = db.Column(db.Integer, primary_key=True)
    genero = db.Column(db.Enum('M', 'F'), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    id_confederacao = db.Column(db.Integer, db.ForeignKey('Confederacao.id'))
    id_modalidade = db.Column(db.Integer, db.ForeignKey('Modalidade.id_modalidade'))
    
    confederacao = db.relationship('Confederacao', back_populates='atletas')
    modalidade = db.relationship('Modalidade', back_populates='atletas')

class Modalidade(db.Model):
    __tablename__ = 'Modalidade'

    id_modalidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    atletas = db.relationship('Atleta', back_populates='modalidade')
