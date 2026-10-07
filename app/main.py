from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2

app = FastAPI(title="Project Template")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/image-info")
async def image_info(file: UploadFile = File(...)):
    data = np.frombuffer(await file.read(), np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    h, w = img.shape[:2]
    return {"filename": file.filename, "width": w, "height": h}