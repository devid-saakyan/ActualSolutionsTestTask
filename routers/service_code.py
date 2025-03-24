from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ServiceCode
from schemas.service_code import ServiceCodeRequest, ServiceCodeResponse

router = APIRouter(prefix="/service_codes", tags=["ServiceCodes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[ServiceCodeResponse])
def get_service_codes(request: ServiceCodeRequest, db: Session = Depends(get_db)):
    return db.query(ServiceCode).limit(request.limit).all()
