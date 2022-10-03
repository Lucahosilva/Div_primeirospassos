from urllib import request
from flask import Flask
from flask import render_template
from flask import redirect, request
import pandas as pd

app = Flask(__name__,)

@app.route('/')
def index():
    print("Hello print")
    return "Hello return"

@app.route('/segunda_rota')   
def segunda():
    return "segunda return"  

@app.route('/hello/<nome>')
def hello(nome):
    return f'olá, {nome}'

produtos={}
@app.route('/listar')
def listar():
    return produtos

@app.route('/adicionar/<produto>/<valor>')
def adicionar(produto, valor):
    produtos[produto] = float(valor)
    return 'Produto adicionado'

@app.route('/cadastro')
def cadastrto():
    argumentos = request.args.to_dict()
    preco =argumentos['preco']
    nome = argumentos['produto']
    produro = argumentos[produtos]
    return argumentos





if __name__ == "__main__":
    app.run()