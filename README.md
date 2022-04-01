# Projeto Ampulheta

O aplicativo tem como público alvo profissionais que tem a necessidade de apontar horas de trabalho em projetos associados.

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