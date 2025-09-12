# Programação Eficaz - Projeto 2

# Projeto: API de Gestão de Imóveis

## Descrição

## Funcionalidades e Rotas

A API deve permitir:

- CHECK **Listar todos os imóveis**  
  `GET /imoveis`  
  Retorna todos os imóveis cadastrados com todos os seus atributos.

- CHECK **Listar um imóvel específico**  
  `GET /imoveis/<id>`  
  Retorna um imóvel pelo seu `id` com todos os seus atributos.

- **Adicionar um novo imóvel**  
  `POST /imoveis`  
  Adiciona um novo imóvel ao banco de dados.

- **Atualizar um imóvel existente**  
  `PUT /imoveis/<id>`  
  Atualiza os dados de um imóvel já existente.

- **Remover um imóvel existente**  
  `DELETE /imoveis/<id>`  
  Remove um imóvel do banco de dados.

- **Listar imóveis por tipo**  
  `GET /imoveis/tipo/<tipo>`  
  Lista todos os imóveis de um determinado tipo (ex: casa, apartamento, terreno).

- **Listar imóveis por cidade**  
  `GET /imoveis/cidade/<cidade>`  
  Lista todos os imóveis localizados em uma determinada cidade.

---

## Testes Automatizados

- Devem ser implementados **testes automatizados para todas as rotas** utilizando, por exemplo, `pytest` ou `unittest`.
- Os testes devem ser escritos **antes da implementação das rotas**, seguindo o princípio de TDD.

---

## Banco de Dados

- Utilizar **MySQL** hospedado na plataforma **Aiven**.
- Para gerar a estrutura do banco de dados, utilize o script SQL disponível.

---

## Deploy

- O projeto deve ser **deployado em uma instância EC2 da AWS**.
- Certifique-se de configurar variáveis de ambiente para os dados sensíveis (ex: conexão com o banco).
