from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import NPI
from schemas.npi import NpiRequest, NpiResponse

router = APIRouter(prefix="/npis", tags=["Npis"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[NpiResponse])
def get_npis(request: NpiRequest, db: Session = Depends(get_db)):
    return db.query(NPI).limit(request.limit).all()
