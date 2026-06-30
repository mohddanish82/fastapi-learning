from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employment_experience: int
    
@app.post("/prediction")
def predict_loan(application: LoanApplication):
    approved = (
        application.income>50000 and application.employment_experience>2 and
        application.age>21 
    )
    return {
        
        "application name": application.name,
        "loan_amount": application.loan_amount,
        "decision": "approved" if approved else "rejected",
        "review_income": application.income
    }
    
    