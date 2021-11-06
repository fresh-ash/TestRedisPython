import redis
import uvicorn
from fastapi import FastAPI

from Response import Response

r = redis.StrictRedis(host='localhost', port=12000, db=0)

app = FastAPI()


@app.get("/")
async def index():
    return "Redis operations"


@app.post("/add")
async def add_command(obj: Response):
    r.set(obj.name, obj.comment)
    return obj


@app.post("/append/{item}")
async def append_to_comment(item: str, obj: Response):

    if r.get(item):
        r.append(item, obj.comment)
        return {"Response": "Successfully"}

    return {"Response": "Bad request"}


@app.get("/commands")
async def get_commands():
    return r.keys()


@app.get("/commands/{item}")
async def get_command(item: str):
    return r.get(item)


@app.delete("/delete/{item}")
async def del_command(item: str):
    r.delete(item)
    return {"Status": "Successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

