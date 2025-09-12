import sqlite3
from dataclasses import dataclass
import mysql
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

print("oi", os.getenv('SSL_CA_PATH'))
# Configurações para conexão com o banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST'),  # Obtém o host do banco de dados da variável de ambiente
    'user': os.getenv('DB_USER'),  # Obtém o usuário do banco de dados da variável de ambiente
    'password': os.getenv('DB_PASSWORD'),  # Obtém a senha do banco de dados da variável de ambiente
    'database': os.getenv('DB_NAME'),  # Obtém o nome do banco de dados da variável de ambiente
    'port': int(os.getenv('DB_PORT')),  # Obtém a porta do banco de dados da variável de ambiente
    'ssl_ca': os.getenv('SSL_CA_PATH')  # Caminho para o certificado SSL
}

def load_template(file_name):
    with open(file_name, encoding='utf-8') as f:
        template = f.read()
    return template


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
    return cur.fetchall()




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