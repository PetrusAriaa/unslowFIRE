from datetime import timedelta, datetime
import os
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import jwt, JWTError

from .db import USER_DATA


class UserAuth(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


auth_router = APIRouter()


def find_user(email: str) -> tuple[int, bool]:
    """
    Return:
    \n`(index: int, is_error: bool)`
    """
    for i, data in enumerate(USER_DATA):
        if email == data["email"]:
            return i, False
    return -1, True


def generate_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, os.getenv("SECRET"), os.getenv("ALGORITHM"))
    return token


@auth_router.post("/", response_model=Token)
def authentication(auth_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Response:
    index, is_error = find_user(auth_data.username)
    if is_error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Email address not found", headers={"WWW-Authenticate": "Bearer"})
    if auth_data.password != USER_DATA[index]["password"]:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Email or password is incorrect", headers={"WWW-Authenticate": "Bearer"})
    token_expire = timedelta(minutes=float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    token = generate_token(data={"agent": USER_DATA[index]["username"]}, expires_delta=token_expire)
    res = JSONResponse({"access_token" : token, "token_type": "bearer"})
    res.headers.append("Set-Cookie", f"TOKEN={token}")
    return res