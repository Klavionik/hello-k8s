import pydantic
from fastapi import FastAPI
import socket
import uvicorn
import os

app = FastAPI()
hostname = socket.gethostname()
secret = os.environ.get("SECRET")


class Hello(pydantic.BaseModel):
    msg: str
    secret: str


@app.get("/hello", response_model=Hello)
async def hello(name: str):
    return {"msg": f"Hello {name} from {hostname}!", "secret": secret}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7777)
