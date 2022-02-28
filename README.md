# Projeto TODO List

Exemplo de um projeto simples com Django.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/luxu/project-biblioteca.git
cd teste_nova_data
python3 -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## Consulta a API

````
import requests
url = "https://project-biblioteca.herokuapp.com/api/books/"
response = requests.get(url)
response.json()
````