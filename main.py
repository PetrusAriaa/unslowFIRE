from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.company import user_route
from routes.auth import auth_router
from dotenv import load_dotenv

origins = [
    "http://localhost:5173",
    "http://localhost"
]

app = FastAPI()
load_dotenv()

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(prefix="/api/v1/company", router=user_route)
app.include_router(prefix="/api/v1/auth", router=auth_router)