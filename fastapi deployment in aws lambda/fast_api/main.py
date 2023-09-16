from typing import Union
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from joblib import load

import pandas as pd

app = FastAPI()
handler = Mangum(app)

model = load("./model.joblib")
y_train = pd.read_csv('./y_train.csv')


def data_validation_and_reform(age,surgery):
    surgery_dict={
        "colostomy":1,
        "ileostomy":2,
        "urostomy":3
    }

    error = False
    message = ''
    data = {}

    if surgery not in surgery_dict:
        error = True
        message = f'option error ->  surgery options are (colostomy or ileostomy or urostomy)'
        data = {}
        return error, message, data
    

    data = {
        "age" : age,
        "surgery" : surgery
    }
    return error, message, data

@app.get("/get_recomendations")
async def read_item(age,surgery):

    error, message, data = data_validation_and_reform(age, surgery)
    if error:
        return{
            "status": 400,
            "message":message
        }
    
    patient_features = pd.DataFrame({"Age": [45],"surgery_numeric":2})
    distances, indices = model.kneighbors(patient_features)
    product_list = y_train.iloc[indices[0]]
    final_product_list = product_list['ProductId'].to_list()
    return {
        "status":200,
        "highly_recomended_product": final_product_list[0],
        "product_list":final_product_list[1:]
    }