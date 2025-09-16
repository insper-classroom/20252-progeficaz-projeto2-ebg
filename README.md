# Programação Eficaz - Projeto 2

## Projeto: API de Gestão de Imóveis

### Descrição

API RESTful para uma empresa imobiliária, desenvolvida em Flask, que permite cadastrar, listar, atualizar, remover e filtrar imóveis em um banco de dados MySQL hospedado na Aiven. O projeto segue princípios de TDD e foi deployado em uma instância EC2 na AWS.

---

### Link da API

Acesse a API em:  
**[https://107.23.164.193/imoveis](https://107.23.164.193/imoveis)**  

---

### Funcionalidades e Rotas

A API permite:

- **Listar todos os imóveis**  
  `GET /imoveis`
- **Listar um imóvel específico**  
  `GET /imoveis/<id>`
- **Adicionar um novo imóvel**  
  `POST /imoveis`
- **Atualizar um imóvel existente**  
  `PUT /imoveis/<id>`
- **Remover um imóvel existente**  
  `DELETE /imoveis/<id>`
- **Listar imóveis por tipo**  
  `GET /imoveis/tipo/<tipo>`
- **Listar imóveis por cidade**  
  `GET /imoveis/cidade/<cidade>`

---

### Testes Automatizados

- Todos os endpoints possuem testes automatizados, escritos **antes da implementação** das rotas (TDD), utilizando `pytest`.

---

### Banco de Dados

- **MySQL** hospedado na plataforma **Aiven**.
- Estrutura do banco criada via script SQL disponível no Handout.

---

### Deploy

- Deploy realizado em uma instância **EC2 da AWS**.
- Variáveis sensíveis (ex: dados de conexão) configuradas por variáveis de ambiente.

---

### Como executar localmente
To be written


### Sobre
Projeto para a disciplina Programação Eficaz - Insper (2025/2).
Desenvolvido por Emily de Britto Gomes