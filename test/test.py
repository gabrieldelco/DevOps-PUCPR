from unittest.mock import patch

import pytest


@pytest.mark.asyncio
def test_root():
    assert root() == {"message": "Hello World"}

@pytest.mark.asyncio
def test_funcaoteste():
    with patch('random.randint', return_value = 12345):
        result = funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
def test_create_estudante():
    estudante_teste = Estudante(nome = "Fulano", curso = "1", ativo = False)
    assert estudante_teste == create_estudante(estudante_teste)

@pytest.mark.asyncio
def test_update_estudante_negativo():
    assert not update_estudante(-5)

@pytest.mark.asyncio
def test_update_estudante_positivo():
    assert update_estudante(10)

@pytest.mark.asyncio
def test_delete_estudante_negativo():
    assert not delete_estudante (-5)

@pytest.mark.asyncio
def test_delete_estudante_positivo():
    assert delete_estudante (10)