from fastapi import APIRouter, Depends

from repositories.retrieve import Retrieve
from db.connection import  db_connect
from schemas import retrieve as schema_r
from schemas import retrieve_users as schema_ru



router = APIRouter()

@router.post('/users')
async def get_users(filters: schema_ru.UsersFilter, database = Depends(db_connect), page: int = 1, limit: int = 10):
    return await Retrieve(db=database).get_users_list(filters=filters, page=page, limit=limit)


@router.post('/items', response_model=schema_r.ItemsResponse)
async def get_items(filters: schema_r.ItemsFilter, 
    order_by: schema_r.OrderBy, 
    database = Depends(db_connect),
    page: int = 1, limit: int = 10):
    return await Retrieve(db=database).get_items(filters=filters, order_by=order_by, page=page, limit=limit)