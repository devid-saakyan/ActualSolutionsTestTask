from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import InNetwork
from schemas.in_network import InNetworkRequest, InNetworkResponse

router = APIRouter(prefix="/in_networks", tags=["InNetworks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[InNetworkResponse])
def get_in_networks(request: InNetworkRequest, db: Session = Depends(get_db)):
    return db.query(InNetwork).limit(request.limit).all()
