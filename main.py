from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(request: LoginRequest):
    if request.username == "user" and request.password == "pass":
        return {"message": "Login successful", "token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/")
async def root():
    return {"message": "Login Microservice is running"}