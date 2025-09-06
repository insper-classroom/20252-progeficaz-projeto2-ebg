from utils import get_imoveis, get_imovel_by_id
from flask import jsonify
    
def index():
    imoveis = get_imoveis()
    return imoveis


def get_imovel(imovel_id):
    imovel = get_imovel_by_id(imovel_id)
    print(f'#'*50)
    print('VIEWS.PY - GET_IMOVEL')
    print(imovel)
    return jsonify(imovel={"id": imovel.id,
                       "logradouro": imovel.logradouro,
                       "tipo_logradouro": imovel.tipo_logradouro,
                       "bairro": imovel.bairro,
                       "cidade": imovel.cidade,
                       "cep": imovel.cep,
                       "tipo": imovel.tipo,
                       "valor": imovel.valor,
                       "data_aquisicao": imovel.data_aquisicao
                       }), 200
