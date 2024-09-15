from typing import List
from core.schemas import DetectionResult
from infrastructure.yolo_model import YOLOModel


class ObjectDetectionService:
    def __init__(self, model: YOLOModel):
        self.model = model

    def detect(self, image_path: str) -> List[DetectionResult]:
        detections = self.model.predict(image_path)

        return detections
