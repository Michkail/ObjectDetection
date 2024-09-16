from ultralytics import YOLO
from core.schemas import DetectionResult
from typing import List


class YOLOModel:
    def __init__(self, model_path: str = 'yolov8l.pt'):
        self.model = YOLO(model_path)

    def predict(self, image_path: str) -> List[DetectionResult]:
        results = self.model.predict(image_path)
        detections = []

        for result in results:
            print(f">>>>>>>>>>>>>>>>>>>>>>> RESULT {result}")
            for bbox, class_name, conf in zip(result.boxes.xyxy, result.names.values(), result.boxes.conf):
                print(f">>>>>>>>>>>>>>>>>>>>>>> CONFIDENCE {conf.item()}")
                print(f">>>>>>>>>>>>>>>>>>>>>>> BBOX {bbox.tolist()}")
                print(f">>>>>>>>>>>>>>>>>>>>>>> CLASS_NAME {class_name}")
                detections.append(DetectionResult(class_name=class_name,
                                                  confidence=conf.item(),
                                                  bbox=bbox.tolist()))

        return detections
