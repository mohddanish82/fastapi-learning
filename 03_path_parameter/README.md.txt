# Path Parameter - FastAPI

A simple FastAPI project demonstrating the use of Path Parameters.

## Features

- Get customer details using Customer ID
- Model prediction endpoint
- JSON responses

## Endpoints

### Get Customer

GET /customer/{customer_id}

Example:

/customer/101

### Model Prediction

GET /model/{model_name}/customer/{customer_id}

Example:

/model/fraud_detector/customer/104

## Run the Project

```bash
pip install fastapi uvicorn
uvicorn path:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Tech Stack

- Python
- FastAPI
- Uvicorn