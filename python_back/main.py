from fastapi import FastAPI
from routes.classification_router import router as reg_route

app = FastAPI()

app.include_router(reg_route)