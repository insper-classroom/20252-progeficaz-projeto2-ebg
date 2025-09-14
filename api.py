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
    

@app.route('/imoveis/<int:imovel_id>', methods=['PUT'])
def update_imovel(imovel_id):
    print(request)
    data = request.get_json()
    
    imoveis = views.update_imovel(imovel_id, data)
    return imoveis


@app.route('/imoveis/<int:imovel_id>', methods=['DELETE'])
def delete_imovel(imovel_id):
    print(request)
    imoveis = views.delete_imovel(imovel_id)
    return imoveis


@app.route('/imoveis/tipo/<type>', methods=['GET'])
def get_imoveis_by_type(type):
    print(request)
    imoveis = views.get_imoveis_by_type(type)
    return imoveis


@app.route('/imoveis/cidade/<city>', methods=['GET'])
def get_imoveis_by_city(city):
    print(request)
    imoveis = views.get_imoveis_by_city(city)
    return imoveis


if __name__ == "__main__":
    app.run(debug=True)