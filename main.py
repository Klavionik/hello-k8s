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


class Ulitochka(pydantic.BaseModel):
    msg: str


@app.get("/hello", response_model=Hello)
async def hello(name: str):
    return {"msg": f"Hello {name} from {hostname}!", "secret": secret, "another_secret": another_secret}


@app.get('/ulitochka', response_model=Ulitochka)
async def ulitochka():
    return {"msg": "ulitochka is so sleepy..."}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7777)
