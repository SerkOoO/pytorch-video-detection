from fastapi import FastAPI,File,UploadFile
from fastapi.responses import JSONResponse
import httpx
from utils.model import predict_video
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:80"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Predict(BaseModel):
    predict: str

predict = None
last_prediction = None
last_video = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload-video")
async def save_video(file: UploadFile = File(...)) -> str:
    global last_video
    contents = await file.read()
    with open(f"test-video/{file.filename}", "wb") as f:
        f.write(contents)
    last_video = f"test-video/{file.filename}"
    return "success"


@app.post("/send-data")
async def send_data() -> JSONResponse:
    global last_prediction
    global last_video

    prediction_result = await predict_video(last_video)  
    last_prediction = prediction_result
    return {
        "response": prediction_result
    }


@app.get("/api/predict")
async def get_last_prediction() -> dict:
    if last_prediction is None:
        return {"message": "pas de predict"}
    return {"last_prediction": last_prediction}

@app.get("/api/lastvideo")
async def get_last_video() -> dict:
    if last_video is None:
        return {"message": "pas de predict"}
    return {"last_prediction": last_video}