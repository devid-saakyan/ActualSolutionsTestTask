from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ProviderGroup
from schemas.provider_group import ProviderGroupRequest, ProviderGroupResponse

router = APIRouter(prefix="/provider_groups", tags=["ProviderGroups"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[ProviderGroupResponse])
def get_provider_groups(request: ProviderGroupRequest, db: Session = Depends(get_db)):
    return db.query(ProviderGroup).limit(request.limit).all()
