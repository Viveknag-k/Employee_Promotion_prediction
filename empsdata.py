from pydantic import BaseModel
class empdata(BaseModel):
    employee_id: int
    no_of_trainings:int
    age:int
    previous_year_rating:float
    length_of_service:int
    awards_won:int
    avg_training_score:float