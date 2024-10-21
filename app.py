from flask import Flask # Biblioteca
from flask import render_template
from flask import request

app = Flask(__name__) # Carregamento

@app.route("/") # Rota
def index(): # Função
    return '<h1>Olá<br>mundo!</h1>'

@app.route("/aluno") # Rota
def aluno(): # Função
    return render_template('formulario.html')

@app.route("/envio", methods=['POST']) # Rota
def envioForms(): # Função
    nombre = request.form['nome']
    senha = request.form['senha']

    if senha == '123':
        return render_template('aluno.html', n = nombre)
    else:
        return 'NAO PASSARÁ!!!!'