from fastapi import APIRouter, Depends

from repositories.retrieve import Retrieve
from db.connection import  db_connect
from schemas import retrieve as schema_r



router = APIRouter()

@router.get('/user/{url}')
async def get_user(url: str, database = Depends(db_connect)):
    crud = Retrieve(db=database)
    user = await crud.get_user_by_profile_link(url)
    return user


@router.post('/items')
async def get_items(filters: schema_r.ItemsFilter, 
    order_by: schema_r.OrderBy, 
    database = Depends(db_connect),
    page: int = 1, limit: int = 10):
    return await Retrieve(db=database).get_items(filters=filters, order_by=order_by, page=page, limit=limit)