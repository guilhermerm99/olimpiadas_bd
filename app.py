from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Chave secreta para mensagens flash

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# CRUD para Atletas
@app.route('/atletas')
def listar_atletas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Atleta")
    atletas = cursor.fetchall()
    conn.close()
    return render_template('atleta.html', atletas=atletas)

@app.route('/atleta/criar', methods=['GET', 'POST'])
def criar_atleta():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        id_confederacao = request.form['id_confederacao']
        id_modalidade = request.form['id_modalidade']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Atleta (nome, genero, data_nasc, id_confederacao, id_modalidade)
            VALUES (%s, %s, %s, %s, %s)
        ''', (nome, genero, data_nasc, id_confederacao, id_modalidade))
        conn.commit()
        conn.close()
        flash('Atleta criado com sucesso!')
        return redirect(url_for('listar_atletas'))
    return render_template('criar_atleta.html')

@app.route('/atleta/editar/<int:id>', methods=['GET', 'POST'])
def editar_atleta(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Atleta WHERE id_atleta = %s', (id,))
    atleta = cursor.fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        id_confederacao = request.form['id_confederacao']
        id_modalidade = request.form['id_modalidade']
        
        cursor.execute('''
            UPDATE Atleta
            SET nome = %s, genero = %s, data_nasc = %s, id_confederacao = %s, id_modalidade = %s
            WHERE id_atleta = %s
        ''', (nome, genero, data_nasc, id_confederacao, id_modalidade, id))
        conn.commit()
        conn.close()
        flash('Atleta atualizado com sucesso!')
        return redirect(url_for('listar_atletas'))
    return render_template('editar_atleta.html', atleta=atleta)

@app.route('/atleta/deletar/<int:id>')
def deletar_atleta(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Atleta WHERE id_atleta = %s', (id,))
    conn.commit()
    conn.close()
    flash('Atleta deletado com sucesso!')
    return redirect(url_for('listar_atletas'))

# Adicione CRUD para Evento e Medalha de forma semelhante.

if __name__ == '__main__':
    app.run(debug=True)
