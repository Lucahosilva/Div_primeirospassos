from flask import Flask
app = Flask(__name__)

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



if __name__ == "__main__":
    app.run()