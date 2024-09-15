import strawberry
from typing import List
from infrastructure.dependencies import get_object_detection_service


@strawberry.type
class DetectionType:
    class_name: str
    confidence: float
    bbox: List[float]


@strawberry.type
class Query:
    @strawberry.field
    def detect_objects(self, image_path: str) -> List[DetectionType]:
        service = get_object_detection_service()
        results = service.detect(image_path)  # Dapatkan hasil deteksi
        print(dir(results))
        detections = []

        # Mengakses data dari hasil deteksi
        for result in results:
            if result.boxes is not None:
                # Ambil informasi dari boxes
                boxes_data = result.boxes.xyxy if hasattr(result.boxes, 'xyxy') else []

                # Ambil nama kelas
                names = result.names if hasattr(result, 'names') else {}

                for box in boxes_data:
                    if len(box) >= 5:  # Pastikan cukup elemen untuk diakses
                        class_id = int(box[5])  # ID kelas dari box
                        confidence = float(box[4])  # Kepercayaan dari box
                        detection = DetectionType(
                            class_name=names.get(class_id, "unknown"),  # Nama kelas dari ID kelas
                            confidence=confidence,  # Kepercayaan dari box
                            bbox=box[:4].tolist()  # Koordinat bounding box
                        )
                        detections.append(detection)

        return detections


schema = strawberry.Schema(query=Query)
