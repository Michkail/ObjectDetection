from domain.object_detection import ObjectDetectionService
from infrastructure.dependencies import get_object_detection_service
from typing import List


def detect_objects(image_path: str) -> List:
    service = get_object_detection_service()

    return service.detect(image_path)
