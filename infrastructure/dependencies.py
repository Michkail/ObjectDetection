from infrastructure.yolo_model import YOLOModel
from domain.object_detection import ObjectDetectionService


def get_yolo_model() -> YOLOModel:
    return YOLOModel()


def get_object_detection_service() -> ObjectDetectionService:
    model = get_yolo_model()

    return ObjectDetectionService(model)
