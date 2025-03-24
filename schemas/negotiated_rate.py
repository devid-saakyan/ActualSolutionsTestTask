from pydantic import BaseModel


class NegotiatedRateRequest(BaseModel):
    limit: int = 10


class NegotiatedRateResponse(BaseModel):
    id: int
    in_network_id: int

    class Config:
        orm_mode = True
