import json
import uuid
from pydantic import BaseModel
from fastapi import APIRouter, Response, status
from time import sleep

from .db import COMPANY_DATA

class Company(BaseModel):
    _id: str | None
    name: str
    head_office: str

user_route = APIRouter()


def dummy_connection(key: int=-1) -> Company:
    sleep(1) # mock database connection
    if key == -1:
        return COMPANY_DATA
    return COMPANY_DATA[key]

@user_route.get("/")
def get_users() -> Response:
    data = dummy_connection()
    res = Response(json.dumps({"error": None, "data": data}))
    res.headers["Content-Type"] = "application/json"
    return res

@user_route.get("/{counter}")
def get_users(counter: int) -> Response:
    if counter < 0:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    data = dummy_connection(counter)
    res = Response(json.dumps({"error": None, "data": data}))
    res.headers["Content-Type"] = "application/json"
    return res

@user_route.post("/")
def create_user(company: Company) -> Response:
    _id = str(uuid.uuid4())
    COMPANY_DATA.append({
        "_id": _id,
        "name": company.name,
        "head_office": company.head_office
    })
    res = Response(json.dumps({"error": None, "message": "Created", "ObjID": _id}))
    return res