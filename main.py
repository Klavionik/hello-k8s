import pydantic
from fastapi import FastAPI, Response
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


class Cat(pydantic.BaseModel):
    msg: str


@app.get("/healthz")
async def healthz():
    return Response(content="OK")


@app.get("/hello", response_model=Hello)
async def hello(name: str):
    return {"msg": f"Hello {name} from {hostname}!", "secret": secret, "another_secret": another_secret}


@app.get("/cat", response_model=Cat)
async def hello(name: str):
    return {"msg": f"Meow {name} from {hostname}!"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7777)
