from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd


# Define the model loading function
def load_model(path: str):
    with open(path, 'rb') as file:
        return pickle.load(file)


# Initialize FastAPI app
app = FastAPI(title="My First FastAPI")


# Load the model
model = load_model("trained_pipeline.pkl")


# Define a Pydantic model for the input data
class Features(BaseModel):
    Cement: float
    Blast_Furnace_Slag: float = None
    Fly_Ash: float = None
    Water: float
    Superplasticizer: float = None
    Coarse_Aggregate: float
    Fine_Aggregate: float
    Age: int


@app.get("/")
async def root():
    return {"healthcheck": "OK"}


@app.post("/predict")
async def predict(features: Features):
    try:
        # Prepare the features to match the model's expected input
        features_dict = features.dict(by_alias=True)
        features_dict = {
            key.replace('_', ' '): value for key, value in features_dict.items() if value is not None
        }
        # Convert the input data to a DataFrame
        input_df = pd.DataFrame([features_dict])
        # Use the model to make predictions
        prediction = model.predict(input_df)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
