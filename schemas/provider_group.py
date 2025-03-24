from typing import Optional

from pydantic import BaseModel


class ProviderGroupRequest(BaseModel):
    limit: int = 10


class ProviderGroupResponse(BaseModel):
    id: int
    provider_reference_id: Optional[int]
    tin_type: Optional[str]
    tin_value: Optional[str]

    class Config:
        orm_mode = True
