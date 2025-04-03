import fastapi

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("teste 1")
async def funcaoteste():
    return {"teste": "deu certo"}


