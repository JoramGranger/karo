from fastapi import APIRouter, HTTPException
from traffic_management.ml_models.route_optimization_model.predict import optimize_route

router = APIRouter()

@router.get("/")
async def calculate_route():
    # Example function to simulate route calculation
    return {"message": "Route calculated"}

@router.post("/optimize")
async def optimize_route_data(data: dict):
    try:
        optimized_route = optimize_route(data)
        return {"optimized_route": optimized_route}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
