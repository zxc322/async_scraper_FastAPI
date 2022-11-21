from pydantic import BaseModel
from typing import Optional, List, Dict

class UsersFilter(BaseModel):
    user_id: Optional[int]
    name: Optional[str]
    profile_url: Optional[str]
    phone: Optional[str]
    type: Optional[str]
    listings: Optional[int]
    website_url: Optional[str]
    on_kijiji_from: Optional[str]
    avg_reply: Optional[str]
    reply_rate: Optional[str]


class UsersResponse(BaseModel):
    response: Optional[List[UsersFilter]] = []
    pagination: Dict