# FastAPI GET Method

This is a simple FastAPI example demonstrating a **GET** endpoint.

## Endpoint

- **GET** `/customer`

### Query Parameter

- `customer_id` (int)

### Example Request

```
http://127.0.0.1:8000/customer?customer_id=1
```

### Example Response

```json
{
  "customer_id": 1,
  "name": "Danish",
  "address": "Kashipur, Uttarakhand",
  "mobile number": "8218097235",
  "status": "active"
}
```

## Technologies Used

- Python
- FastAPI
- Uvicorn