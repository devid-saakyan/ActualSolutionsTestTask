from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import BillingCodeModifier
from schemas.billing_code_modifier import BillingCodeModifierRequest, BillingCodeModifierResponse

router = APIRouter(prefix="/billing_code_modifiers", tags=["BillingCodeModifiers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=list[BillingCodeModifierResponse])
def get_billing_code_modifiers(request: BillingCodeModifierRequest, db: Session = Depends(get_db)):
    return db.query(BillingCodeModifier).limit(request.limit).all()
