import strawberry
from typing import List
from strawberry.file_uploads import Upload
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
        results = service.detect(image_path)

        return [DetectionType(**result.dict()) for result in results]


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def detect_objects(self, file: Upload) -> List[DetectionType]:
        service = get_object_detection_service()
        file_location = f"temp/{file.filename}"

        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())

        results = service.detect(file_location)

        return [DetectionType(**result.dict()) for result in results]


schema = strawberry.Schema(query=Query, mutation=Mutation)
