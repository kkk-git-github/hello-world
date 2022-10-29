from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/my-api")

class user:
    name = str()
    email = str()
    password = str()
    def getuserinfo():
        name = input("Enter your name")
        email = input("Enter your email")
        password = input("Enter your password")
        