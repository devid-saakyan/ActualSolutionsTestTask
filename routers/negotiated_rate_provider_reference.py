from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import NegotiatedRateProviderReference
from schemas.negotiated_rate_provider_reference import NegotiatedRateProviderReferenceRequest, NegotiatedRateProviderReferenceResponse

router = APIRouter(prefix="/negotiated_rate_provider_references", tags=["NegotiatedRateProviderReferences"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[NegotiatedRateProviderReferenceResponse])
def get_negotiated_rate_provider_references(request: NegotiatedRateProviderReferenceRequest, db: Session = Depends(get_db)):
    return db.query(NegotiatedRateProviderReference).limit(request.limit).all()
