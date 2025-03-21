from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DetectionResult(Base):
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    xmin = Column(Float)
    ymin = Column(Float)
    xmax = Column(Float)
    ymax = Column(Float)
    confidence = Column(Float)
    class_label = Column(String)