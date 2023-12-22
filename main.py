from fastapi import FastAPI
from routes.company import user_route
from routes.auth import auth_router

app = FastAPI()

app.include_router(prefix="/api/v1/company", router=user_route)
app.include_router(prefix="/api/v1/auth", router=auth_router)