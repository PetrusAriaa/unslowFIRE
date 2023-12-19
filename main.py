from fastapi import FastAPI
from routes.company import user_route

app = FastAPI()

app.include_router(prefix="/api/v1/company", router=user_route)