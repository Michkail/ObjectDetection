from ultralytics import YOLO
from core.schemas import DetectionResult
from typing import List


class YOLOModel:
    def __init__(self, model_path: str = 'yolov8n.pt'):
        self.model = YOLO(model_path)

    def predict(self, image_path: str) -> List[DetectionResult]:
        results = self.model.predict(image_path)
        print(dir(results))
        detections = []

        for result in results:
            for bbox, class_name, conf in zip(result.boxes.xyxy, result.names, result.conf):
                detections.append(DetectionResult(class_name=class_name,
                                                  confidence=conf.item(),
                                                  bbox=bbox.tolist()))

        return detections
