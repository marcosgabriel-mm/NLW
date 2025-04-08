# Sistema de Gerenciamento de Eventos NLW
Este é um sistema de gerenciamento de eventos desenvolvido em Python utilizando Flask como framework web, SQLAlchemy para ORM e SQLite como banco de dados.

## Estrutura do Projeto
O projeto segue uma arquitetura em camadas:
- API REST: Rotas disponibilizadas via Flask
- Handlers: Manipuladores de requisições
- Repositórios: Acesso a dados
- Entidades: Modelos de dados
- Utilitários: Tratamento de erros, tipos HTTP

## Funcionalidades
Eventos
- Criação de eventos
- Consulta de eventos por ID
- Controle de lotação de eventos

## Participantes
- Registro de participantes em eventos
- Consulta de crachá de participante
- Listagem de participantes por evento

Check-in
- Registro de check-in de participantes

## Como executar
1. Clone o repositório
2. Crie um ambiente virtual Python:
```python3
python -m venv venv
```

3. Ative o ambiente virtual:
```python3
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```python3
pip install flask flask-cors sqlalchemy pytest
```
6. Crie o banco de dados:
```python3
sqlite3 storage.db < init/schema.sql
```
7. Execute a aplicação:
```python3
python app.py
```

O servidor estará disponível em http://localhost:3000

## Rotas da API
Eventos
- POST /events - Cria um novo evento
- GET /events/{event_id} - Obtém informações de um evento

Participantes
- POST /events/{event_id}/register - Registra um participante em um evento
- GET /attendees/{attendee_id}/badge - Obtém o crachá de um participante
- GET /events/{event_id}/attendees - Lista participantes de um evento

Check-in
- POST /attendees/{attendee_id}/check-in - Registra check-in de um participante

## Testes
Para executar os testes:
```python3
pytest
```

## Tecnologias Utilizadas
- Flask
- SQLAlchemy
- SQLite
- Python 3
SQLAlchemy
SQLite
Python 3
