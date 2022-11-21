import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)


from sqlalchemy import Boolean, Column, SmallInteger, ForeignKey, Integer, String, DateTime
from datetime import datetime

from db.connection import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    profile_url = Column(String)
    phone = Column(String, nullable=True)
    type = Column(String)
    listings = Column(SmallInteger)
    website_url = Column(String, nullable=True)
    on_kijiji_from = Column(String, nullable=True)
    avg_reply = Column(String, nullable=True)
    reply_rate = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    ad_id = Column(String)
    creator_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String)
    location = Column(String)
    address = Column(String)
    published_date = Column(DateTime)
    price = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    description = Column(String)


class OverView(Base):
    __tablename__ = "overview"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.item_id'))
    hydro = Column(Boolean)
    heat = Column(Boolean)
    water = Column(Boolean)
    wifi = Column(Boolean)
    parking = Column(SmallInteger)
    agreement_type = Column(String, nullable=True)
    move_in_date = Column(String, nullable=True)
    pet_friendly = Column(String, nullable=True)


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.item_id'))
    size = Column(SmallInteger, nullable=True)
    furnished = Column(Boolean)
    laundry_in_unit = Column(Boolean)
    lundry_in_building = Column(Boolean)
    dishwasher = Column(Boolean)
    fridge = Column(Boolean)
    air_conditioning = Column(Boolean)
    balcony = Column(Boolean)
    yard = Column(Boolean) 
    smoking_permitted = Column(Boolean)


users_table = User.__table__
items_table = Item.__table__
overviews_table = OverView.__table__
units_table = Unit.__table__
