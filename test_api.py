import pytest
from api import app
from utils import connect_db
from unittest.mock import patch, MagicMock


# 1. FIXTURE
@pytest.fixture
def client():
    """
    Fixture: configura um ambiente de teste e fornece os dados necessários para os testes.
    Nesse caso, o cliente de teste simula o usuário da plataforma de Imóveis.
    """
    app.config['TEST'] = True
    with app.test_client() as client:
        yield client


# ========================================================================================== 1. GET ==========================================================================================


# 2. PATCH 
@patch('utils.connect_db') # Ou seja, a função a ser substituída é, no arquivo api.py, a 'connect_db'
# WHEN 
def test_get_imoveis(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    
    # Simulando um banco de dados
    mock_cursor.fetchall.return_value = [
        (0, 'Apartamento', "Rua 1", "Nº 1", "Bairro 1", "Araras", "SP"),
        (1, 'Apartamento', "Rua 2", "Nº 2", "Bairro 2", "Araras", "SP"),
        (2, 'Apartamento', "Rua 3", "Nº 3", "Bairro 3", "Araras", "SP"),
    ]
    
    
    mock_connect_db.return_value = mock_conn # Mandamos o Mock ser retornado quando a função for chaamda
    response = client.get('/imoveis')
    
    
    # THEN
    assert response.status_code == 200
    expected_response = {
        'imoveis': [
            {'id': 0, 'tipo': 'Apartamento', 'Rua': 'Rua 1', 'Numero': 'Nº 1', 'Bairro': 'Bairro 1', 'Cidade': 'Araras', 'Estado': 'SP'},
            {'id': 1, 'tipo': 'Apartamento', 'Rua': 'Rua 2', 'Numero': 'Nº 2', 'Bairro': 'Bairro 2', 'Cidade': 'Araras', 'Estado': 'SP'},
            {'id': 2, 'tipo': 'Apartamento', 'Rua': 'Rua 3', 'Numero': 'Nº 3', 'Bairro': 'Bairro 3', 'Cidade': 'Araras', 'Estado': 'SP'},
        ]
    }
    assert response.get_json() == expected_response
    
    
# ========================================================================================== 2. GET/<ID> ==========================================================================================


@pytest.mark.parametrize(
    'imovel_id, esperado, mock_result',
    [
        (0, {'id': 0, 'tipo': 'Apartamento', 'Rua': 'Rua 1', 'Numero': 'Nº 1', 'Bairro': 'Bairro 1', 'Cidade': 'Araras', 'Estado': 'SP'},
            [(0, 'Apartamento', "Rua 1", "Nº 1", "Bairro 1", "Araras", "SP")]),
        (1, {'id': 1, 'tipo': 'Apartamento', 'Rua': 'Rua 2', 'Numero': 'Nº 2', 'Bairro': 'Bairro 2', 'Cidade': 'Araras', 'Estado': 'SP'},
            [(1, 'Apartamento', "Rua 2", "Nº 2", "Bairro 2", "Araras", "SP")]),
        (2, {'id': 2, 'tipo': 'Apartamento', 'Rua': 'Rua 3', 'Numero': 'Nº 3', 'Bairro': 'Bairro 3', 'Cidade': 'Araras', 'Estado': 'SP'},
            [(2, 'Apartamento', "Rua 3", "Nº 3", "Bairro 3", "Araras", "SP")]),
    ]
)

@patch('utils.connect_db') # Ou seja, a função a ser substituída é, no arquivo api.py, a 'connect_db'

def test_get_imovel(mock_connect_db, client, imovel_id, esperado, mock_result):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchall.return_value = mock_result
    
    
    mock_connect_db.return_value = mock_conn
    response = client.get(f'/imoveis/{imovel_id}')
    
    # THEN
    assert response.status_code == 200
    assert response.get_json() == {'imovel': esperado}