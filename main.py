import pydantic
from fastapi import FastAPI
import socket
import uvicorn
import os

app = FastAPI()
hostname = socket.gethostname()
secret = os.environ.get("SECRET")
another_secret = os.environ.get("ANOTHER_SECRET")


class Hello(pydantic.BaseModel):
    msg: str
    secret: str
    another_secret: str


class Goodbye(pydantic.BaseModel):
    msg: str


@app.get("/hello", response_model=Hello)
async def hello(name: str):
    return {"msg": f"Hello {name} from {hostname}!", "secret": secret, "another_secret": another_secret}


@app.get("/goodbye", response_model=Goodbye)
async def goodbye(name: str):
    return {"msg": f"Goodbye, {name}! We'll miss ya."}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7777)
