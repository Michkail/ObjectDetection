from pydantic import BaseModel
from typing import List


class DetectionResult(BaseModel):
    class_name: str
    confidence: float
    bbox: List[float]
