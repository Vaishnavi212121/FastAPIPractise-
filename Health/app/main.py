from fastapi import FastAPI
from app.routers.health_router import router


app = FastAPI()

app.include_router(router)