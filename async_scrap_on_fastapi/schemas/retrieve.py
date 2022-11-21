from pydantic import BaseModel, root_validator
from typing import Optional, List, Dict
from datetime import date

class ResponseId(BaseModel):
    id: int


class OrderBy(BaseModel):
    order_by: Optional[List[str]] = ['published_date']

    @root_validator
    def check_list_length(cls, values):
        order_possible = ('published_date', 'published_date DESC', 'price', 'price DESC', 'size', 'size DECS')
        order_list = values.get('order_by')
        if order_list:
            for el in order_list:
                if el not in order_possible:
                    raise ValueError(f'Possible orders [{order_possible}].')    
        return values


class ItemsFilter(BaseModel):
    ad_id: Optional[str]
    creator_id: Optional[int]
    title: Optional[str]
    location: Optional[str]
    address: Optional[str]
    published_date: Optional[List[date]]
    price: Optional[List[int]]

    hydro: Optional[bool]
    heat: Optional[bool]
    water: Optional[bool]
    wifi: Optional[bool]
    parking: Optional[int]
    agreement_type: Optional[str]
    move_in_date: Optional[str]
    pet_friendly: Optional[str]

    size: Optional[List[int]]
    furnished: Optional[bool]
    laundry_in_unit: Optional[bool]
    lundry_in_building: Optional[bool]
    dishwasher: Optional[bool]
    fridge: Optional[bool]
    dishwasher: Optional[bool]
    air_conditioning: Optional[bool]
    balcony: Optional[bool]
    yard: Optional[bool]
    smoking_permitted: Optional[bool]

    @root_validator
    def check_list_length(cls, values):
        dates = values.get('published_date')
        prices = values.get('price')
        size = values.get('size')
        if dates and len(dates) != 2:
            raise ValueError('List must have 2 elements inside.')
        if prices and len(prices) != 2:
            raise ValueError('List must have 2 elements inside.')
        if size:
            if len(size) != 2 or (size[0]<0 or size[1]>32000):
                raise ValueError('List must have 2 elements inside. Expected values (0 ... 32,000)')    
        return values

    
class ItemsData(BaseModel):
    ad_id: str    
    title: Optional[str]
    location: Optional[str]
    address: Optional[str]
    published_date: Optional[date]
    price: Optional[int]

    creator_id: int
    creator_name: str
    creator_profile: str
    phone: Optional[str]
    creators_total_listings: Optional[int]
    on_kijiji_from: Optional[str]
    reply_rate: Optional[str] 
    avg_reply: Optional[str]

    hydro: bool
    heat: bool
    water: bool
    wifi: bool
    parking: int
    agreement_type: Optional[str]
    move_in_date: Optional[str]
    pet_friendly: Optional[str]

    size: Optional[int]
    furnished: bool
    laundry_in_unit: bool
    lundry_in_building: bool
    dishwasher: bool
    fridge: bool
    dishwasher: bool
    air_conditioning: bool
    balcony: bool
    yard: bool
    smoking_permitted: bool
    description: Optional[str]


class ItemsResponse(BaseModel):
    response: Optional[List[ItemsData]] = []
    pagination: Dict