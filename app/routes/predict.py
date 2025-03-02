from fastapi import APIRouter
from app.schemas.request import InputData
from app.services.inference import predict

router = APIRouter()

@router.post("/predict/")
def predict_ml(data: InputData):
    return predict(data.features)
