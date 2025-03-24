from pydantic import BaseModel


class BillingCodeModifierRequest(BaseModel):
    limit: int = 10


class BillingCodeModifierResponse(BaseModel):
    id: int
    negotiated_price_id: int
    modifier: str

    class Config:
        orm_mode = True
