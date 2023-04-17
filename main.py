from fastapi import FastAPI
import socket
import uvicorn

app = FastAPI()
hostname = socket.gethostname()


@app.get("/hello")
async def hello(name: str):
    return {"msg": f"Hello {name} from {hostname}!\n"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7777)
