from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ProviderReference
from schemas.provider_reference import ProviderReferenceRequest, ProviderReferenceResponse

router = APIRouter(prefix="/provider_references", tags=["ProviderReferences"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[ProviderReferenceResponse])
def get_provider_references(request: ProviderReferenceRequest, db: Session = Depends(get_db)):
    return db.query(ProviderReference).limit(request.limit).all()
