# Rodando via Docker
- Dentro da pasta *backend*, rodar um `docker-compose up` e acessar a aplicação pela porta `5000`

# Rodando localmente
- Criar ambiente virtual `python -m venv .env`
- Ativar ambiente virtual `souurce .env/bin/activate`
- Intalar dependências `pip install -r requirements.txt`
- Iniciar em modo debug `FLASK_DEBUG=1 python -m flask run`

# Obs
- No [app.py](src/app.py) tem vários exemplos de rotas e como serví-las e [aqui](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) deve ter 90% do que a gente vai precisar pra esse MVP.
- Na pasta [src/static](src/static) estão nossos arquivos estáticos, os serviços podem consumir dali, fiz um endpoint `/api/user` como exemplo

# TODO
- Vou arrumar o docker-compose pra podermos debuggar mesmo via docker, deve dar pra fazer um `attach` pelo VSCODE na porta `5678`





