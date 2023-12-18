from fastapi import FastAPI
from routes.user import user_route

app = FastAPI()

app.include_router(prefix="/api/v1/users", router=user_route)