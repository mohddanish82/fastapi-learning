from fastapi import FastAPI
app = FastAPI()

customers = [
    {"id":1001,"name":"Danish","city":"delhi","risk":"low"},
    {"id":1001,"name":"Om","city":"mumbai","risk":"high"},
    {"id":1001,"name":"Rakesh","city":"delhi","risk":"low"},
    {"id":1001,"name":"Abhishek","city":"mumbai","risk":"high"},
    {"id":1001,"name":"Priya","city":"delhi","risk":"low"}
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered=[
        c for c in customers
           if c["city"] == city and c["risk"] == risk
    ]
    
    return {
        
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "result": filtered
    }
    
    
    
    