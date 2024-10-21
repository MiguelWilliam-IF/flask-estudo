from flask import Flask # Biblioteca

app = Flask(__name__) # Carregamento

@app.route("/") # Rota
def index(): # Função
    return '<h1>Olá<br>mundo!</h1>'

@app.route("/aluno/<nome>") # Rota
def aluno(nome): # Função
    return f'<h1>meu nome é {nome}</h1>'
