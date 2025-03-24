from pydantic import BaseModel


class NpiRequest(BaseModel):
    limit: int = 10


class NpiResponse(BaseModel):
    id: int
    provider_group_id: int
    value: str

    class Config:
        orm_mode = True
