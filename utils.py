import sqlite3


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