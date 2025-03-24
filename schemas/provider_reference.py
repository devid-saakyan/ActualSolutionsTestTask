from pydantic import BaseModel


class ProviderReferenceRequest(BaseModel):
    limit: int = 10


class ProviderReferenceResponse(BaseModel):
    id: int
    provider_group_id: int

    class Config:
        orm_mode = True
