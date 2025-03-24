from pydantic import BaseModel


class ServiceCodeRequest(BaseModel):
    limit: int = 10


class ServiceCodeResponse(BaseModel):
    id: int
    negotiated_price_id: int
    code: str

    class Config:
        orm_mode = True
