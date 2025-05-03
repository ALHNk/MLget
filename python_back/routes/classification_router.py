from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import knn_model
from services import classification_services as class_serv


router = APIRouter(prefix="/classification")

class QueryRequest(BaseModel):
    query: str
    model: str
    dataset:str

@router.get("/")
def func():
    return "hello"

@router.post("/predict")
def predict(request: QueryRequest):
    print(f"router:{request.query} ")
    answer = class_serv.predict(request.query, request.model, request.dataset)
    return {"prediction": answer}

@router.post("/train")
def train(request: QueryRequest):
    print("Started training")
    answer = class_serv.train(request.model, request.dataset)
    return {"answer": answer}