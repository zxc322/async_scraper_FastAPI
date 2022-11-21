import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from repositories.generic import GenericInit
from repositories.services.multifilter import MultiFilter
from sqlalchemy import select, func
from typing import Optional
import math

from schemas import retrieve as schema_r
from repositories.services.pagination import paginate_data


class Retrieve(GenericInit):

    async def get_items(
        self, filters: schema_r.ItemsFilter, 
        order_by: schema_r.OrderBy,
        page: int = 1, limit: int = 10 ) -> schema_r.ItemsResponse:
        """ Returns paginated items list """

        page = 1 if page<1 else page
        skip = (page-1) * limit
        end = skip + limit
        filters = filters.dict(skip_defaults=True)

        query_gen = MultiFilter(filters=filters, order_by=order_by.order_by, limit=limit, offset=skip)
        query = query_gen.retrieve_item()
        count_query = query_gen.get_count()
        print(f'-- count query {query} ---')
        count = await self.db.fetch_one(query=count_query)

        count=count.total_items

        total_pages = math.ceil(count/limit)
        pagination = await paginate_data(page=page, count=count, total_pages=total_pages, end=end, limit=limit, url='items')
        return schema_r.ItemsResponse(response=await self.db.fetch_all(query), pagination=pagination)

        
    async def get_user_by_profile_link(self, link: str) -> Optional[int]:
        user = await self.db.fetch_one(select(self.users.c.user_id).select_from(
            self.users).where(
                self.users.c.profile_url==link)
        )
        return user.user_id if user else None

    async def get_item_by_ad_ID(self, ad_id: int) -> Optional[int]:
        item = await self.db.fetch_one(select(self.items.c.item_id).select_from(
            self.items).where(
                self.items.c.ad_id==ad_id)
        )
        return item

