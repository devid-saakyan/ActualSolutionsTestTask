from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import NegotiatedPrice
from schemas.negotiated_price import NegotiatedPriceRequest, NegotiatedPriceResponse

router = APIRouter(prefix="/negotiated_prices", tags=["NegotiatedPrices"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[NegotiatedPriceResponse])
def get_negotiated_prices(request: NegotiatedPriceRequest, db: Session = Depends(get_db)):
    return db.query(NegotiatedPrice).limit(request.limit).all()
