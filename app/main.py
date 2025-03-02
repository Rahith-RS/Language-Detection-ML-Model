from fastapi import FastAPI
from app.routes import detect

app = FastAPI(title="Language Detection API")

# Include the route
app.include_router(detect.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Language Detection Model is running!"}
