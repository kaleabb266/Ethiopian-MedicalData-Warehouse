from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_name: str
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    class_label: str

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True