from random import randint
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": randint(a:0, b: 57000)}


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante


@app.put("/estudante/update/{id_estudante}"
async def update_estudante(id_estudante: int):
        return id_estudante > 0


@app.delete("estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
        return id_estudante




