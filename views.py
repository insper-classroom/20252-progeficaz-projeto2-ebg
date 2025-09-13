from utils import get_imoveis, get_imovel_by_id
from flask import jsonify
    
def index():
    imoveis = get_imoveis()
    return jsonify(imoveis)


def get_imovel(imovel_id):
    imovel = get_imovel_by_id(imovel_id)
    return jsonify(imovel.__dict__)
