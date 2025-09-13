from flask import Flask, redirect, request
import views


app = Flask(__name__)


@app.route('/imoveis', methods=['GET'])
def index():
    print(request)
    imoveis = views.index()
    return imoveis


@app.route('/imoveis/<imovel_id>', methods=['GET'])
def get_imovel(imovel_id):
    print(request)
    imovel = views.get_imovel(imovel_id) 
    return imovel


@app.route('/imoveis', methods=['POST'])
def add_imovel():
    print(request)
    
    data = request.get_json()
    logradouro = data['logradouro']
    tipo_logradouro = data['tipo_logradouro']
    bairro = data['bairro']
    cidade = data['cidade']
    cep = data['cep']
    tipo = data['tipo']
    valor = data['valor']
    data_aquisicao = data['data_aquisicao']
    imoveis = views.add_imovel(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
    return imoveis
    



if __name__ == "__main__":
    app.run(debug=True)
    