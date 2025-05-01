from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import knn_model
from services import classification_services as class_serv


router = APIRouter(prefix="/classification")

class QueryRequest(BaseModel):
    query: str
    model: str

@router.get("/")
def func():
    return "hello"

@router.post("/predict")
def predict(request: QueryRequest):
    print(f"router:{request.query} ")
    answer = class_serv.predict(request.query, request.model)
    return {"prediction": answer}

@router.post("/train")
def train(request: QueryRequest):
    answer = class_serv.train(request.model)
    return {"answer": answer}