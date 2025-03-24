from pydantic import BaseModel


class NegotiatedPriceRequest(BaseModel):
    limit: int = 10


class NegotiatedPriceResponse(BaseModel):
    id: int
    negotiated_rate_id: int
    negotiated_type: str
    negotiated_rate: float
    expiration_date: str
    billing_class: str

    class Config:
        orm_mode = True
