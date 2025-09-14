from utils import get_imoveis, get_imovel_by_id, add_imovel_to_db, update_data_on_imovel, delete_imovel_from_db, get_imoveis_by_type_name, get_imoveis_by_city_name
from flask import jsonify
    
    
def index():
    imoveis = get_imoveis()
    return jsonify(imoveis)


def get_imovel(imovel_id):
    imovel = get_imovel_by_id(imovel_id)
    return jsonify(imovel.__dict__)


def add_imovel(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao):
    imoveis = add_imovel_to_db(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
    return jsonify(imoveis)


def update_imovel(imovel, data):
    imoveis = update_data_on_imovel(imovel, data)
    return jsonify(imoveis)


def delete_imovel(imovel):
    imoveis = delete_imovel_from_db(imovel)
    return jsonify(imoveis)


def get_imoveis_by_type(type):
    imoveis = get_imoveis_by_type_name(type)
    return jsonify(imoveis) 


def get_imoveis_by_city(city):
    imoveis = get_imoveis_by_city_name(city)
    return jsonify(imoveis)
