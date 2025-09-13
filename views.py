from utils import get_imoveis, get_imovel_by_id, add_imovel_to_db
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