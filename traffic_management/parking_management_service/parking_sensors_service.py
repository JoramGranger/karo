from fastapi import APIRouter, HTTPException
from traffic_management.ml_models.parking_model.predict import predict_parking

router = APIRouter()

@router.get("/availability")
async def get_parking_availability():
    return {"message": "Parking availability"}

@router.post("/predict")
async def predict_parking_data(data: dict):
    try:
        prediction = predict_parking(data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
