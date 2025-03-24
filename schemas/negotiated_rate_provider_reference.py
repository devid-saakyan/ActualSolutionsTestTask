from pydantic import BaseModel


class NegotiatedRateProviderReferenceRequest(BaseModel):
    limit: int = 10


class NegotiatedRateProviderReferenceResponse(BaseModel):
    id: int
    negotiated_rate_id: int
    reference_id: int

    class Config:
        orm_mode = True
