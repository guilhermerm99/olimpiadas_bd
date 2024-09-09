from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Pais, Confederacao, Atleta

# Rotas para País
def listar_paises():
    paises = Pais.query.all()
    return render_template('paises.html', paises=paises)

def criar_pais():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_pais = Pais(nome=nome)
        try:
            db.session.add(novo_pais)
            db.session.commit()
            flash('País criado com sucesso!', 'success')
            return redirect(url_for('listar_paises'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao criar país: {e}', 'danger')
    return render_template('criar_pais.html')

def editar_pais(id):
    pais = Pais.query.get_or_404(id)
    if request.method == 'POST':
        pais.nome = request.form['nome']
        try:
            db.session.commit()
            flash('País atualizado com sucesso!', 'success')
            return redirect(url_for('listar_paises'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar país: {e}', 'danger')
    return render_template('editar_pais.html', pais=pais)

def deletar_pais(id):
    pais = Pais.query.get_or_404(id)
    try:
        db.session.delete(pais)
        db.session.commit()
        flash('País deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar país: {e}', 'danger')
    return redirect(url_for('listar_paises'))

# Rotas para Confederação
def listar_confederacoes():
    confederacoes = Confederacao.query.all()
    return render_template('confederacoes.html', confederacoes=confederacoes)

def criar_confederacao():
    paises = Pais.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        pais_id = request.form['pais_id']
        nova_confederacao = Confederacao(nome=nome, pais_id=pais_id)
        try:
            db.session.add(nova_confederacao)
            db.session.commit()
            flash('Confederação criada com sucesso!', 'success')
            return redirect(url_for('listar_confederacoes'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao criar confederação: {e}', 'danger')
    return render_template('criar_confederacao.html', paises=paises)

def editar_confederacao(id):
    confederacao = Confederacao.query.get_or_404(id)
    paises = Pais.query.all()
    if request.method == 'POST':
        confederacao.nome = request.form['nome']
        confederacao.pais_id = request.form['pais_id']
        try:
            db.session.commit()
            flash('Confederação atualizada com sucesso!', 'success')
            return redirect(url_for('listar_confederacoes'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar confederação: {e}', 'danger')
    return render_template('editar_confederacao.html', confederacao=confederacao, paises=paises)

def deletar_confederacao(id):
    confederacao = Confederacao.query.get_or_404(id)
    try:
        db.session.delete(confederacao)
        db.session.commit()
        flash('Confederação deletada com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar confederação: {e}', 'danger')
    return redirect(url_for('listar_confederacoes'))

# Rotas para Atleta
def listar_atletas():
    atletas = Atleta.query.all()
    return render_template('atletas.html', atletas=atletas)

def criar_atleta():
    paises = Pais.query.all()
    confederacoes = Confederacao.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        pais_id = request.form['pais_id']
        confederacao_id = request.form['confederacao_id']
        novo_atleta = Atleta(nome=nome, genero=genero, data_nasc=data_nasc,
                             pais_id=pais_id, confederacao_id=confederacao_id)
        try:
            db.session.add(novo_atleta)
            db.session.commit()
            flash('Atleta criado com sucesso!', 'success')
            return redirect(url_for('listar_atletas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao criar atleta: {e}', 'danger')
    return render_template('criar_atleta.html', paises=paises, confederacoes=confederacoes)

def editar_atleta(id):
    atleta = Atleta.query.get_or_404(id)
    paises = Pais.query.all()
    confederacoes = Confederacao.query.all()
    if request.method == 'POST':
        atleta.nome = request.form['nome']
        atleta.genero = request.form['genero']
        atleta.data_nasc = request.form['data_nasc']
        atleta.pais_id = request.form['pais_id']
        atleta.confederacao_id = request.form['confederacao_id']
        try:
            db.session.commit()
            flash('Atleta atualizado com sucesso!', 'success')
            return redirect(url_for('listar_atletas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar atleta: {e}', 'danger')
    return render_template('editar_atleta.html', atleta=atleta, paises=paises, confederacoes=confederacoes)

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
