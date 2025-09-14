from utils import get_imoveis, get_imovel_by_id, add_imovel_to_db, update_data_on_imovel, delete_imovel_from_db, get_imoveis_by_type_name, get_imoveis_by_city_name
from flask import jsonify
    
    
def index():
    imoveis = get_imoveis()
    return jsonify(imoveis), 200


def get_imovel(imovel_id):
    imovel = get_imovel_by_id(imovel_id)
    if imovel is None:
        return jsonify({"erro": "Imóvel não encontrado"}), 404
    return jsonify(imovel.__dict__), 200


def add_imovel(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao):
    novo_imovel = add_imovel_to_db(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
    return jsonify(novo_imovel.__dict__), 201



def update_imovel(imovel_id, data):
    imovel_existente = get_imovel_by_id(imovel_id)
    if imovel_existente is None:
        return jsonify({'erro': 'Imóvel não encontrado'}), 404

    imovel_atualizado = update_data_on_imovel(imovel_id, data)
    return jsonify(imovel_atualizado.__dict__), 200



def delete_imovel(imovel_id):
    result = delete_imovel_from_db(imovel_id)
    if not result:
        return jsonify({'erro': 'Imóvel não encontrado'}), 404
    return '', 204 # Como apaguei o imóvel, o padrão REST é que não retornar nada


def get_imoveis_by_type(type):
    imoveis = get_imoveis_by_type_name(type)
    return jsonify(imoveis), 200


def get_imoveis_by_city(city):
    imoveis = get_imoveis_by_city_name(city)
    return jsonify(imoveis), 200
