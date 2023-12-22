import json
from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from .db import USER_DATA

auth_router = APIRouter()

class UserAuth(BaseModel):
    email: str
    password: str

def find_user(email: str) -> tuple[int, bool]:
    """
    Return:
    \n`(index: int, is_error: bool)`
    """
    for i, data in enumerate(USER_DATA):
        if email == data["email"]:
            return i, False
    return -1, True

@auth_router.post("/")
def authentication(auth_data: UserAuth) -> Response:
    index, is_error = find_user(auth_data.email)
    if is_error:
        return Response(json.dumps({"message" : "Data Not Found"}), status_code=status.HTTP_404_NOT_FOUND)
    if auth_data.password != USER_DATA[index]["password"]:
        return Response(json.dumps({"message" : "Unauthorized"}), status_code=status.HTTP_403_FORBIDDEN)    
    return Response(json.dumps({"message" : "ok"}), status_code=status.HTTP_200_OK)