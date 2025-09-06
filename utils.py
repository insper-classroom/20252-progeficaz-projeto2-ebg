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
            'tipo': row[1],
            'Rua': row[2],
            'Numero': row[3],
            'Bairro': row[4],
            'Cidade': row[5],
            'Estado': row[6]
        })
    return imoveis


def get_imovel(imovel_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM imoveis WHERE id = ?', (imovel_id,))
    rows = cur.fetchall()
    conn.close()
    imovel = []
    for row in rows:
        imovel.append({
            'id': row[0],
            'tipo': row[1],
            'Rua': row[2],
            'Numero': row[3],
            'Bairro': row[4],
            'Cidade': row[5],
            'Estado': row[6]
        })
    return imovel