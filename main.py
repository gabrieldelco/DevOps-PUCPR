from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return{"messsage": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return{"teste": True, "num_aleatorio": random.randint(0, 1000)}