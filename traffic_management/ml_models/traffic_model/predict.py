import joblib
import pandas as pd
from .preprocess import preprocess_input

# Load the model
model = joblib.load('traffic_management/ml_models/traffic_model/traffic_model_v1.pkl')

def predict_traffic(data: dict):
    # Preprocess the input data
    input_data = preprocess_input(data)
    df = pd.DataFrame([input_data])
    
    # Predict using the loaded model
    prediction = model.predict(df)
    return prediction.tolist()
