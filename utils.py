import sqlite3
from dataclasses import dataclass


@dataclass
class Imovel:
    id: int 
    logradouro: str
    tipo_logradouro: str
    bairro: str
    cidade: str
    cep: str
    tipo: str
    valor: float
    data_aquisicao: str


def connect_db():
    return sqlite3.connect('imoveis.sql')


def get_imoveis():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM imoveis')
    rows = cur.fetchall()
    conn.close()
    imoveis = []
    for row in rows:
        imoveis.append({
            'id': row[0],
            'logradouro': row[1],
            'tipo_logradouro': row[2],
            'bairro': row[3],
            'cidade': row[4],
            'cep': row[5],
            'tipo': row[6],
            'valor': row[7],
            'data_aquisicao': row[8]
        })
    return imoveis


def get_imovel_by_id(imovel_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM imoveis WHERE id = ?', (imovel_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    print(f'*'*50)
    print('UTILS.PY - GET_IMOVEL_BY_ID')
    return Imovel(
        id=row[0],             
        logradouro= row[1],
        tipo_logradouro= row[2],
        bairro= row[3],
        cidade= row[4],
        cep= row[5],
        tipo= row[6],
        valor= row[7],
        data_aquisicao= row[8])