# ClienteAPI - Projeto Django com SQLite

## Visão Geral

ClienteAPI é uma aplicação de gerenciamento de clientes construída com Django e utilizando SQLite como banco de dados. Esta aplicação permite realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em um banco de dados de clientes

## Funcionalidades

- Listar todos os clientes
- Visualizar detalhes de um cliente específico
- Adicionar um novo cliente
- Atualizar informações de um cliente existente
- Remover um cliente

## Tecnologias Utilizadas
- Django 3.2
- SQLite
- Django REST Framework (DRF)

## Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/django__api-clientes.git
cd django__api-clientes
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado):

- Linux/Mac:
  
```bash
python -m venv venv
source venv/bin/activate
```

- Windows:
  
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

## Autor

- Pericles Matos
