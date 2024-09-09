from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Atleta, Evento, Medalha

# Rotas para Atleta
@app.route('/atletas')
def listar_atletas():
    atletas = Atleta.query.all()
    return render_template('atleta.html', atletas=atletas)

@app.route('/atleta/criar', methods=['GET', 'POST'])
def criar_atleta():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        id_confederacao = request.form['id_confederacao']
        id_modalidade = request.form['id_modalidade']
        novo_atleta = Atleta(nome=nome, genero=genero, data_nasc=data_nasc,
                             id_confederacao=id_confederacao, id_modalidade=id_modalidade)
        try:
            db.session.add(novo_atleta)
            db.session.commit()
            flash('Atleta criado com sucesso!', 'success')
            return redirect(url_for('listar_atletas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao criar atleta: {e}', 'danger')
    return render_template('criar_atleta.html')

@app.route('/atleta/editar/<int:id>', methods=['GET', 'POST'])
def editar_atleta(id):
    atleta = Atleta.query.get_or_404(id)
    if request.method == 'POST':
        atleta.nome = request.form['nome']
        atleta.genero = request.form['genero']
        atleta.data_nasc = request.form['data_nasc']
        atleta.id_confederacao = request.form['id_confederacao']
        atleta.id_modalidade = request.form['id_modalidade']
        try:
            db.session.commit()
            flash('Atleta atualizado com sucesso!', 'success')
            return redirect(url_for('listar_atletas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar atleta: {e}', 'danger')
    return render_template('editar_atleta.html', atleta=atleta)

@app.route('/atleta/deletar/<int:id>', methods=['GET', 'POST'])
def deletar_atleta(id):
    atleta = Atleta.query.get_or_404(id)
    try:
        db.session.delete(atleta)
        db.session.commit()
        flash('Atleta deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar atleta: {e}', 'danger')
    return redirect(url_for('listar_atletas'))

# Rotas para Evento e Medalha seguem o mesmo padrão das rotas de Atleta
