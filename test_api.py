import pytest
from api import app
from utils import connect_db
from unittest.mock import patch, MagicMock
from utils import Imovel

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
    (0, 'Rua 1', 'Rua', 'Bairro 1', 'Araras', '12345-000', 'Apartamento', 350000.0, '2023-01-10'),
    (1, 'Rua 2', 'Rua', 'Bairro 2', 'Araras', '12345-001', 'Apartamento', 360000.0, '2023-02-10'),
    (2, 'Rua 3', 'Rua', 'Bairro 3', 'Araras', '12345-002', 'Apartamento', 370000.0, '2023-03-10')]
    

    mock_connect_db.return_value = mock_conn # Mandamos o Mock ser retornado quando a função for chaamda
    response = client.get('/imoveis')
    
    
    # THEN
    assert response.status_code == 200
    expected_response = [
        {
        'id': 0,
        'logradouro': 'Rua 1',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 1',
        'cidade': 'Araras',
        'cep': '12345-000',
        'tipo': 'Apartamento',
        'valor': 350000.0,
        'data_aquisicao': '2023-01-10'
        },
        {
        'id': 1,
        'logradouro': 'Rua 2',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 2',
        'cidade': 'Araras',
        'cep': '12345-001',
        'tipo': 'Apartamento',
        'valor': 360000.0,
        'data_aquisicao': '2023-02-10'
        },
        {
        'id': 2,
        'logradouro': 'Rua 3',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 3',
        'cidade': 'Araras',
        'cep': '12345-002',
        'tipo': 'Apartamento',
        'valor': 370000.0,
        'data_aquisicao': '2023-03-10'
    }]
        
    assert response.get_json() == expected_response
    
    
# ========================================================================================== 2. GET/<ID> ==========================================================================================

@pytest.mark.parametrize(
    'imovel_id, esperado, mock_result',
    [
        (0,
            {'id': 0,
                'logradouro': 'Rua 1',
                'tipo_logradouro': 'Rua',
                'bairro': 'Bairro 1',
                'cidade': 'Araras',
                'cep': '12345-000',
                'tipo': 'Apartamento',
                'valor': 350000.0,
                'data_aquisicao': '2023-01-10'},
            (0,
                'Rua 1',
                'Rua',
                'Bairro 1',
                'Araras',
                '12345-000',
                'Apartamento',
                350000.0,
                '2023-01-10')
        ),
        (1,
            {'id': 1,
                'logradouro': 'Rua 2',
                'tipo_logradouro': 'Rua',
                'bairro': 'Bairro 2',
                'cidade': 'Araras',
                'cep': '12345-001',
                'tipo': 'Apartamento',
                'valor': 360000.0,
                'data_aquisicao': '2023-02-10'},
            (1,'Rua 2',
                'Rua',
                'Bairro 2',
                'Araras',
                '12345-001',
                'Apartamento',
                360000.0,
                '2023-02-10')
        ),
        (2,
            {'id': 2,
                'logradouro': 'Rua 3',
                'tipo_logradouro': 'Rua',
                'bairro': 'Bairro 3',
                'cidade': 'Araras',
                'cep': '12345-002',
                'tipo': 'Apartamento',
                'valor': 370000.0,
                'data_aquisicao': '2023-03-10'},
            (2,
                'Rua 3',
                'Rua',
                'Bairro 3',
                'Araras',
                '12345-002',
                'Apartamento',
                370000.0,
                '2023-03-10')
            )])

@patch('utils.connect_db')

# WHEN 
def test_get_imovel(mock_connect_db, client, imovel_id, esperado, mock_result):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = mock_result
    
    
    mock_connect_db.return_value = mock_conn
    response = client.get(f'/imoveis/{imovel_id}')
    
    # THEN
    assert response.status_code == 200
    assert response.get_json() == esperado


# ========================================================================================== 3. POST - ADICIONAR NOVO IMÓVEL ==========================================================================================
@patch('utils.connect_db')

# WHEN 
def test_add_imovel(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchall.return_value = [
    (0, 'Rua 1', 'Rua', 'Bairro 1', 'Araras', '12345-000', 'Apartamento', 350000.0, '2023-01-10'),
    (1, 'Rua 2', 'Rua', 'Bairro 2', 'Araras', '12345-001', 'Apartamento', 360000.0, '2023-02-10'),
    (2, 'Rua 3', 'Rua', 'Bairro 3', 'Araras', '12345-002', 'Apartamento', 370000.0, '2023-03-10'),
    (3, 'Rua 4', 'Rua', 'Bairro 4', 'Araras', '12345-002', 'Apartamento', 380000.0, '2023-04-10')]
    
    
    mock_connect_db.return_value = mock_conn
    
    response = client.post('/imoveis', json={
        'logradouro': 'Rua 4',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 4',
        'cidade': 'Araras',
        'cep': '12345-002',
        'tipo': 'Apartamento',
        'valor': 380000.0,
        'data_aquisicao': '2023-04-10'
    }
)
    
    # THEN
    assert response.status_code == 200
    expected_response = [
        {
        'id': 0,
        'logradouro': 'Rua 1',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 1',
        'cidade': 'Araras',
        'cep': '12345-000',
        'tipo': 'Apartamento',
        'valor': 350000.0,
        'data_aquisicao': '2023-01-10'
        },
        {
        'id': 1,
        'logradouro': 'Rua 2',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 2',
        'cidade': 'Araras',
        'cep': '12345-001',
        'tipo': 'Apartamento',
        'valor': 360000.0,
        'data_aquisicao': '2023-02-10'
        },
        {
        'id': 2,
        'logradouro': 'Rua 3',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 3',
        'cidade': 'Araras',
        'cep': '12345-002',
        'tipo': 'Apartamento',
        'valor': 370000.0,
        'data_aquisicao': '2023-03-10'
        },
        {
        'id': 3,
        'logradouro': 'Rua 4',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro 4',
        'cidade': 'Araras',
        'cep': '12345-002',
        'tipo': 'Apartamento',
        'valor': 380000.0,
        'data_aquisicao': '2023-04-10'
        }
        ]

        
    assert response.get_json() == expected_response
    

# ========================================================================================== 4. PUT - MODIFICAR INFORMAÇÕES ==========================================================================================
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("imovel_id, update_data, esperado", [
    (
        0,
        {"valor": 400000.0},
        (0, "Rua 1", "Rua", "Bairro 1", "Araras", "12345-000", "Apartamento", 400000.0, "2023-01-10")
    ),
    (
        1,
        {"logradouro": "Avenida Brasil"},
        (1, "Avenida Brasil", "Rua", "Bairro 2", "Araras", "12345-001", "Apartamento", 360000.0, "2023-02-10")
    ),
    (
        2,
        {"bairro": "Centro"},
        (2, "Rua 3", "Rua", "Centro", "Araras", "12345-002", "Apartamento", 370000.0, "2023-03-10")
    ),
    (
        3,
        {"cep": "99999-999"},
        (3, "Rua 4", "Rua", "Bairro 4", "Araras", "99999-999", "Apartamento", 300000.0, "2023-04-10")
    ),
])
@patch("utils.connect_db")
def test_update_imovel(mock_connect_db, imovel_id, update_data, esperado, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Estado esperado após update
    mock_cursor.fetchall.return_value = [
        (0, "Rua 1", "Rua", "Bairro 1", "Araras", "12345-000", "Apartamento", 400000.0, "2023-01-10"),
        (1, "Avenida Brasil", "Rua", "Bairro 2", "Araras", "12345-001", "Apartamento", 360000.0, "2023-02-10"),
        (2, "Rua 3", "Rua", "Centro", "Araras", "12345-002", "Apartamento", 370000.0, "2023-03-10"),
        (3, "Rua 4", "Rua", "Bairro 4", "Araras", "99999-999", "Apartamento", 300000.0, "2023-04-10"),
    ]

    mock_connect_db.return_value = mock_conn

    response = client.put(f"/imoveis/{imovel_id}", json=update_data)
    assert response.status_code == 200

    data = response.get_json()
    atualizado = None
    for imovel in data:
        if imovel["id"] == imovel_id:
            atualizado = imovel
            break

    assert atualizado["id"] == esperado[0]
    assert atualizado["logradouro"] == esperado[1]
    assert atualizado["tipo_logradouro"] == esperado[2]
    assert atualizado["bairro"] == esperado[3]
    assert atualizado["cidade"] == esperado[4]
    assert atualizado["cep"] == esperado[5]
    assert atualizado["tipo"] == esperado[6]
    assert atualizado["valor"] == esperado[7]
    assert atualizado["data_aquisicao"] == esperado[8]
