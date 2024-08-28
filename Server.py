from typing import Union
import joblib
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

model = joblib.load('./model.joblib')

class HouseData(BaseModel):
    Rooms: int
    Bathroom: float
    Landsize: float
    Lattitude:float 
    Longtitude: float


@app.post("/")
def read_root(data:HouseData):
    dict_data = dict(data)
    return model.predict(dict_data)
