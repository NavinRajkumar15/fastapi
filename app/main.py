from fastapi import FastAPI

from app import models
from app.db import engine
from app.routers import router

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)

