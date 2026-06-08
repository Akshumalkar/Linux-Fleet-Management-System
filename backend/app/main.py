from fastapi import FastAPI

app = FastAPI(
    title="Linux Fleet Management Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Linux Fleet Management Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }