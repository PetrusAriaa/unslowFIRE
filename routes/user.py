import json
from typing import Any
from fastapi import APIRouter, Response, status
from time import sleep

from .db import dummy_db

user_route = APIRouter()

def dummy_connection(key: int=-1) -> Any:
    sleep(1)
    if key == -1:
        return dummy_db
    return dummy_db[key]

@user_route.get("/")
def get_users() -> Response:
    data = dummy_connection()
    res = Response(json.dumps({"data": data}))
    res.headers["Content-Type"] = "application/json"
    return res

@user_route.get("/{counter}")
def get_users(counter: int) -> Response:
    if counter < 0:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    data = dummy_connection(counter)
    res = Response(json.dumps({"data": data}))
    res.headers["Content-Type"] = "application/json"
    return res