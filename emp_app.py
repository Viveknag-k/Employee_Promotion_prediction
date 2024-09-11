from fastapi import FastAPI
import pandas as pd
import numpy as np
import pickle
import uvicorn
from empsdata import empdata

app=FastAPI()
pickle_in = open("rf.pkl","rb")
rf = pickle.load(pickle_in)
@app.get('/')
async def index():
    return "Hello, User"

@app.post('/predict')
async def predict_emp(data:empdata):
    data = data.dict()
    print(data)
    print("HELLO")
    
    employee_id = data['employee_id']
    no_of_trainings = data['no_of_trainings']
    age = data['age']
    previous_year_rating = data['previous_year_rating']
    length_of_service = data['length_of_service']
    awards_won = data['awards_won']
    avg_training_score = data['avg_training_score']
    
    print(rf.predict([[employee_id,no_of_trainings,age,previous_year_rating,length_of_service,awards_won,avg_training_score]]))
    predictor = rf.predict([[employee_id,no_of_trainings,age,previous_year_rating,length_of_service,awards_won,avg_training_score]])
    
    if(predictor[0]>0.5):
        return "The Employee will Promote"
    else:
        return "The Employee will not Promote"
    return {
        'prediction':prediction
    }
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)