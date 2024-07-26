import joblib
import pandas as pd
from .preprocess import preprocess_input

# Load the model
model = joblib.load('traffic_management/ml_models/route_optimization_model/route_optimization_model_v1.pkl')

def optimize_route(data: dict):
    # Preprocess the input data
    input_data = preprocess_input(data)
    df = pd.DataFrame([input_data])
    
    # Predict using the loaded model
    optimized_route = model.predict(df)
    return optimized_route.tolist()
