from fastapi import APIRouter, UploadFile, File
from infrastructure.dependencies import get_object_detection_service

router = APIRouter()


@router.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    service = get_object_detection_service()
    contents = await file.read()
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(contents)

    detections = service.detect(file_path)

    return {"detections": [det.dict() for det in detections]}
