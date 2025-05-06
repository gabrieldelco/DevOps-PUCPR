from fastapi import FastAPI
import random
app = FastAPI()

# Alterando os nomes dos endpoints
@app.get("/helloworld")
async def root():
    return{"messsage": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": True, "num_aleatorio": random.randint(0, 50000)}