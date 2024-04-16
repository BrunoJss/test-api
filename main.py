from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"teste":"testado"}


@app.get("/cpf")
def cpf():
    return "API fast"