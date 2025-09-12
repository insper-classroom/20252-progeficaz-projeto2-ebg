from utils import get_imoveis, get_imovel_by_id, load_template, get_imoveis
from flask import jsonify
    
def index():
    imovel_template = load_template('static/templates/components/imovel.html')
    imoveis_li = [
        imovel_template.format(id= row[0],
            logradouro=row[1],
            tipo_logradouro=row[2],
            bairro=row[3],
            cidade=row[4],
            cep=row[5],
            tipo=row[6],
            valor=row[7],
            data_aquisicao=row[8]) for row in get_imoveis()]
    imovel = '\n'.join(imoveis_li)
    return load_template('static/templates/index.html').format(imovel=imovel)



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
