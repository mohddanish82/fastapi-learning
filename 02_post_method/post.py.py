from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    employment_experience: int
    
@app.post("/predict")
def predict_loan(application: LoanApplication):
    
    
    if application.income> 60000 and application.employment_experience> 3:
        decision = "approve ho gya loan ok koi tension nahi lena ka ab "
        
    else:
        decision = "rejected application because you are not eligible for loan ok"
        
    return {
        "application age":application.age,
        "decision":decision
    }
    
    
    
    

