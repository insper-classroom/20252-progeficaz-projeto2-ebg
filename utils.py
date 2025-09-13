import sqlite3
from dataclasses import dataclass
import mysql
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

# Configurações para conexão com o banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST'),  # Obtém o host do banco de dados da variável de ambiente
    'user': os.getenv('DB_USER'),  # Obtém o usuário do banco de dados da variável de ambiente
    'password': os.getenv('DB_PASSWORD'),  # Obtém a senha do banco de dados da variável de ambiente
    'database': os.getenv('DB_NAME'),  # Obtém o nome do banco de dados da variável de ambiente
    'port': int(os.getenv('DB_PORT')),  # Obtém a porta do banco de dados da variável de ambiente
    'ssl_ca': os.getenv('SSL_CA_PATH')  # Caminho para o certificado SSL
}


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
    
    # Armazenando os imóveis em dataclasses e elas em dicionários
    imoveis = []
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
    
    # Retornando o imóvel em dataclass
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
    

def add_imovel_to_db(logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao))
        print("Commitando...")
        conn.commit()
        cur.close()
        conn.close()
        print("Buscando imóveis atualizados...")
        imoveis_atualizado = get_imoveis()
        return imoveis_atualizado
    except Exception as e:
            print("ERRO AO INSERIR:", e)
            raise