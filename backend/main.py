from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginData(BaseModel):
    email: str
    password: str


@app.post("/api/login")
async def login(data: LoginData):
    print("Email:", data.email)
    print("Password:", data.password)

    return {
        "message": "Login successful",
        "email": data.email
    }