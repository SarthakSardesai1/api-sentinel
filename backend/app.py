from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Sentinel Backend is Running"}