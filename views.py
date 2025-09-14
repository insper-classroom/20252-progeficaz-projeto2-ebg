from utils import get_imoveis, get_imovel_by_id, add_imovel_to_db, update_data_on_imovel, delete_imovel_from_db, get_imoveis_by_type_name, get_imoveis_by_city_name
from flask import jsonify
from hypermedia import *
    
'''
Trata os erros e chama as funções que manipulam o banco de dados.
Para tal, passa como argumentos as infos necessárias para cada função e coloca o retorno delas em JSON para o retorno da API.
'''

def index():
    imoveis = get_imoveis()
    for imovel in imoveis:
        imovel["links"] = imovel_links(imovel)
    return jsonify(imoveis), 200



def get_imovel(imovel_id):
    imovel = get_imovel_by_id(imovel_id)
    if imovel is None:
        return jsonify({
            "erro": "Imóvel não encontrado",
            "codigo": 404
        }), 404
    imovel_dict = imovel.__dict__
    imovel_dict["links"] = imovel_links(imovel)
    return jsonify(imovel_dict), 200


def add_imovel(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao):
    novo_imovel = add_imovel_to_db(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
    imovel_dict = novo_imovel.__dict__
    imovel_dict["links"] = imovel_links(novo_imovel)
    return jsonify(imovel_dict), 201


def update_imovel(imovel_id, data):
    imovel_existente = get_imovel_by_id(imovel_id)
    if imovel_existente is None:
        return jsonify({"erro": "Imóvel não encontrado", "codigo": 404}), 404
    imovel_atualizado = update_data_on_imovel(imovel_id, data)
    imovel_dict = imovel_atualizado.__dict__
    imovel_dict["links"] = imovel_links(imovel_atualizado)
    return jsonify(imovel_dict), 200


def delete_imovel(imovel_id):
    result = delete_imovel_from_db(imovel_id)
    if not result:
        return jsonify({
  "erro": "Imóvel não encontrado",
  "codigo": 404
}
), 404
    return '', 204 # Como apaguei o imóvel, o padrão REST é que não retornar nada


def get_imoveis_by_type(type):
    imoveis = get_imoveis_by_type_name(type)
    for imovel in imoveis:
        imovel["links"] = imovel_links(imovel)
    return jsonify(imoveis), 200


def get_imoveis_by_city(city):
    imoveis = get_imoveis_by_city_name(city)
    for imovel in imoveis:
        imovel["links"] = imovel_links(imovel)
    return jsonify(imoveis), 200