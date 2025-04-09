from src.main import *
from random import random
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste_com_random():
    result = await funcaoteste()
    assert result["teste"] is True
    assert isinstance(result["num_aleatorio"], int)
    assert 0 <= result["num_aleatorio"] <= 57000

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool
