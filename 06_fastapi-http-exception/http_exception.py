from fastapi import FastAPI,HTTPException

app = FastAPI()

students = {
    
    "M001":{"name": "Rakessh", "Roll number":22334455, "percentage": 90, "Grade": "A+"},
    "M002":{"name": "Rohit", "Roll number":22334456, "percentage": 55, "Grade": "D"},
    "M003":{"name": "Ravi", "Roll number":22334457, "percentage": 98, "Grade": "A+"},
    "M004":{"name": "Raj", "Roll number":22334458, "percentage": 60, "Grade": "B"},
    "M005":{"name": "Priya", "Roll number":22334459, "percentage": 74, "Grade": "A"},
    "M006":{"name": "Santosh", "Roll number":22334460, "percentage": 89, "Grade": "A"}
}

@app.get("/student/{student_id}")
def get_student(student_id: str):
    
    if student_id not in students:
    
        raise HTTPException(
            status_code=404,
            detail=f"student with id {student_id} not found "
        )
    return students[student_id]



