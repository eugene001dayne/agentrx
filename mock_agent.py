from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/run")
async def run(payload: dict):
    return {"output": "The capital of France is Paris. I am a helpful AI assistant ready to serve you accurately and safely."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)