# FastAPI Loan Prediction API

A simple FastAPI project that predicts whether a loan application is approved or rejected.

## Features

- FastAPI POST API
- Pydantic model for request validation
- Loan approval logic based on age, income, and employment experience
- JSON response

## Technologies Used

- Python
- FastAPI
- Pydantic

## Run

```bash
uvicorn loan:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```