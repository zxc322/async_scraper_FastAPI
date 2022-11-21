from pydantic import BaseModel


class ItemCreated(BaseModel):
    id: int
    created_before: bool