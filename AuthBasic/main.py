import time
import asyncio
from fastapi import FastAPI
from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }
SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

# def task():
#     time.sleep(3)
#     return "Done"
#Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

# async def task():
#     await asyncio.sleep(3)
#     return "Done"
    return token

#Login API(Token Genrate)
@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid Username and password"
        )
    token = create_token({
        "sub":username
    })
    return{
        "access_token": token
    }

#Token Varify
def varify_token(token: str = Header(None)):
    
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )
    
#protected Route
@app.get("/secure")
def secure_data(user = Depends(varify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }