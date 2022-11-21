import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from typing import Dict, Optional
from datetime import datetime

from repositories.generic import GenericInit
from repositories.retrieve import Retrieve
from schemas import retrieve as schema_r
from schemas import create as schema_c


class Insert(GenericInit):

    async def get_or_create_user(self, user_data: Dict) -> int:
        user = await Retrieve(db=self.db).get_user_by_profile_link(user_data.get('profile_url'))
        if user:
            return user
        user_data.update(created_at=datetime.utcnow())
        user_id = await self.db.execute(self.users.insert().values(user_data))
        return user_id

    
    async def get_or_create_item(self, item_data: Dict, user_data: Dict) -> Optional[schema_r.ResponseId]:
        item = await Retrieve(db=self.db).get_item_by_ad_ID(item_data.get('ad_id'))
        if item:
            return schema_c.ItemCreated(id=item.item_id, created_before=True)
        user_id = await self.get_or_create_user(user_data=user_data)
        item_data.update(created_at=datetime.utcnow(), creator_id=user_id)

        if item_data.get('published_date'):
            item_data['published_date'] = datetime.strptime(item_data['published_date'], "%Y-%m-%dT%H:%M:%S.%fZ")

        item_id = await self.db.execute(self.items.insert().values(item_data))
        return schema_c.ItemCreated(id=item_id, created_before=False)

    async def create_overview(self, item_id: int, overview_dict: Dict) -> schema_r.ResponseId:
        overview_dict.update(item_id=item_id)
        return schema_r.ResponseId(id = await self.db.execute(self.overview.insert().values(overview_dict)))


    async def create_units(self, item_id: int, units_dict: Dict) -> schema_r.ResponseId:
        units_dict.update(item_id=item_id)
        return schema_r.ResponseId(id=await self.db.execute(self.units.insert().values(units_dict)))