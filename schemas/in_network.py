from pydantic import BaseModel


class InNetworkRequest(BaseModel):
    limit: int = 10


class InNetworkResponse(BaseModel):
    id: int
    negotiation_arrangement: str
    name: str
    billing_code_type: str
    billing_code_type_version: str
    billing_code: str
    description: str

    class Config:
        orm_mode = True
