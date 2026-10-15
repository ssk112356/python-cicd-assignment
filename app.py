from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the CI/CD Pipeline API!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)