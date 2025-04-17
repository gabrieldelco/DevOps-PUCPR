from fastapi import FastAPI

app = FastAPI()

# Alterando os nomes dos endpoints
@app.get("/helloworld")
async def root():
    return{"messsage": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": "deu certo"}