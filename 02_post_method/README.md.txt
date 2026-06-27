# FastAPI POST Method - Loan Prediction

This is a simple FastAPI example demonstrating a **POST** endpoint using **Pydantic** for request validation.

## Endpoint

- **POST** `/predict`

### Request Body

```json
{
  "age": 25,
  "income": 70000,
  "loan_amount": 500000,
  "employment_experience": 5
}
```

### Example Response (Approved)

```json
{
  "application age": 25,
  "decision": "approve laon"
}
```

### Example Response (Rejected)

```json
{
  "application age": 22,
  "decision": "rejected loan"
}
```

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn