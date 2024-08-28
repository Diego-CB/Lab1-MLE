from typing import Union
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

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
    df = {
        'Rooms': [dict_data['Rooms']],
        'Bathroom': [dict_data['Bathroom']],
        'Landsize': [dict_data['Landsize']],
        'Lattitude': [dict_data['Lattitude']],
        'Longtitude': [dict_data['Longtitude']]
    }

    print(df)

    df = pd.DataFrame(df)
    value = model.predict(df)
    print(value)
    return {"predicted":value[0]}
