from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"messsage": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return{"teste": "deu certo"}