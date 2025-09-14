import sqlite3
from dataclasses import dataclass
import mysql
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


load_dotenv()
# Configurações para conexão c/ banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST'),  
    'user': os.getenv('DB_USER'),  
    'password': os.getenv('DB_PASSWORD'), 
    'database': os.getenv('DB_NAME'),  
    'port': int(os.getenv('DB_PORT')), 
    'ssl_ca': os.getenv('SSL_CA_PATH')
}


# Classe para os imóveis
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
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as err:
        print(f"Erro: {err}")
        return None


def get_imoveis():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM imoveis')
    imoveis_rows = cur.fetchall()
    cur.close()
    conn.close()
    imoveis = [] # Armazenando os imóveis em dataclasses e elas em dicionários
    for row in imoveis_rows:
        imovel = Imovel(
            id=row[0],             
            logradouro= row[1],
            tipo_logradouro= row[2],
            bairro= row[3],
            cidade= row[4],
            cep= row[5],
            tipo= row[6],
            valor= row[7],
            data_aquisicao= row[8])
        imoveis.append(imovel.__dict__)
    return imoveis


def get_imovel_by_id(imovel_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM imoveis WHERE id = %s', (imovel_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return Imovel(id=row[0],             
        logradouro= row[1],
        tipo_logradouro= row[2],
        bairro= row[3],
        cidade= row[4],
        cep= row[5],
        tipo= row[6],
        valor= row[7],
        data_aquisicao= row[8])
    

def add_imovel_to_db(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao))
    conn.commit()
    novo_id = cur.lastrowid
    cur.close()
    conn.close()
    return get_imovel_by_id(novo_id)

        
def update_data_on_imovel(imovel_id, data):
    conn = connect_db()
    cur = conn.cursor()
    set_clause = ", ".join([f"{campo} = %s" for campo in data.keys()])
    values = list(data.values())
    values.append(imovel_id)
    sql = f"UPDATE imoveis SET {set_clause} WHERE id = %s"
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()
    return get_imovel_by_id(imovel_id)


def delete_imovel_from_db(imovel_id):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute('SELECT id FROM imoveis WHERE id = %s', (imovel_id,))
        exists = cur.fetchone()
        if not exists:
            cur.close()
            return False
        cur.execute('DELETE FROM imoveis WHERE id = %s', (imovel_id,))
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def get_imoveis_by_type_name(tipo):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM imoveis WHERE tipo = %s', (tipo,))
        rows = cur.fetchall()
        cur.close()
        chaves = ["id", "logradouro", "tipo_logradouro", "bairro", "cidade", "cep", "tipo", "valor", "data_aquisicao"]
        imoveis = [dict(zip(chaves, row)) for row in rows]
        return imoveis
    finally:
        conn.close()


def get_imoveis_by_city_name(cidade):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM imoveis WHERE cidade = %s', (cidade,))
        rows = cur.fetchall()
        cur.close()
        chaves = ["id", "logradouro", "tipo_logradouro", "bairro", "cidade", "cep", "tipo", "valor", "data_aquisicao"]
        imoveis = [dict(zip(chaves, row)) for row in rows]
        return imoveis
    except Exception as e:
        raise e
    finally:
        conn.close()
