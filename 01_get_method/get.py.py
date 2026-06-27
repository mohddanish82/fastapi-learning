from fastapi import FastAPI

app = FastAPI()

@app.get("/customer")
def get_customer(customer_id: int):
    return {
        "customer_id": customer_id,
        "name":"Danish",
        "address":"kashipur Uttrakhand",
        "mobile number":"8218097235",
        "status":"active"
    }
    
    
