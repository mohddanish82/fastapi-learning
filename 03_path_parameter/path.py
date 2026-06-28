from fastapi import FastAPI
app = FastAPI()

customer_profiles={
    101:{"name":"danish","address":"delhi","risk":"low","score":0.23},
    102:{"name":"ravi","address":"mumbai","risk":"medium","score":0.54},
    103:{"name":"rakesh","address":"noida","risk":"high","score":0.78},
    104:{"name":"ram","address":"delhi","risk":"high","score":0.85},
    105:{"name":"rohit","address":"pune","risk":"low","score":0.32},
    106:{"name":"mohan","address":"bangalore","risk":"low","score":0.19}
    

}

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    if customer_id not in customer_profiles:
        return {"error":f"customer {customer_id} not found"}
    
    profile = customer_profiles[customer_id]
    return{
        "customer_id": customer_id,
        "name": profile["name"],
        "address": profile["address"],
        "risk": profile["risk"],
        "score": profile["score"]
    }
    
    
@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name: str, customer_id: int):
    return{
        "model": model_name,
        "customer_id": customer_id,
        "prediction": "high_risk"
    }
    
    