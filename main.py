from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users_db = [User(name="Mavro", surname="Rojas",
                 url="https://mavrojas.com", age=50)]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q_value: Union[str, None] = None):
    return {"item_id": item_id, "q": q_value}


@app.get("/users")
async def get_users():
    return users_db
