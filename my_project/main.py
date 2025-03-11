from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ethiopian Medical Data Warehouse API"}

@app.post("/detection_results/", response_model=schemas.DetectionResult)
def create_detection_result(detection_result: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
    return crud.create_detection_result(db=db, detection_result=detection_result)

@app.get("/detection_results/", response_model=list[schemas.DetectionResult])
def read_detection_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detection_results = crud.get_detection_results(db, skip=skip, limit=limit)
    return detection_results