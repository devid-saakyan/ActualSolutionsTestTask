from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import NegotiatedRate
from schemas.negotiated_rate import NegotiatedRateRequest, NegotiatedRateResponse

router = APIRouter(prefix="/negotiated_rates", tags=["NegotiatedRates"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[NegotiatedRateResponse])
def get_negotiated_rates(request: NegotiatedRateRequest, db: Session = Depends(get_db)):
    return db.query(NegotiatedRate).limit(request.limit).all()
