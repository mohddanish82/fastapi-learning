# FastAPI Query Parameters

This is a simple FastAPI project that demonstrates how to use **Query Parameters** to filter customer data.

## Features

- Search customers using query parameters
- Filter by city
- Filter by risk level
- Returns matching customers with total count

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Run the Project

1. Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

2. Start the server

```bash
uvicorn main:app --reload
```

## Example Request

```text
http://127.0.0.1:8000/customers?city=delhi&risk=low
```

## Example Response

```json
{
  "city": "delhi",
  "risk": "low",
  "count": 3,
  "result": [
    {
      "id": 1001,
      "name": "Danish",
      "city": "delhi",
      "risk": "low"
    }
  ]
}
```

## What I Learned

- FastAPI Query Parameters
- API filtering
- List Comprehension
- Returning JSON responses