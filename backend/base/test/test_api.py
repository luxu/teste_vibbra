import pytest
from django.contrib.auth.models import User

from backend.base.models import Tempo, Projeto


@pytest.fixture
def usuario(db):
    user = User(
        first_name="João Vitor Correia Martins",
        email="jvcm@luxu.com.br",
        username="jvcm",
        password="jvcm182012",
    )
    user.save()
    return user


@pytest.fixture
def tempo(db):
    time = Tempo(
        started_at="2006-08-09",
        ended_at="2006-08-09",
        projeto_id=1
    )
    time.save()
    return time


@pytest.fixture
def projeto(db):
    project = Projeto()
    project.save()
    return project


def test_times():
    ...


def test_criar_tempo(tempo):
    assert tempo is None


def test_criar_projeto(projeto):
    assert projeto is None
    # assert projeto.title == 'Fala Freud'


def test_carregar_usuario(usuario):
    assert usuario.username == 'jvcm'
