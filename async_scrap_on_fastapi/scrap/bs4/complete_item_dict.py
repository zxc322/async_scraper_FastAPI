from scrap.bs4.item_parse_methods import BS4Parse



class CompleteDict:

    def __init__(self, cls: BS4Parse) -> None:
        self.parse = cls


    async def user_insert(self):
        user = dict(
            name = await self.parse.creator_name(),
            profile_url = await self.parse.profile_url(),
            phone = await self.parse.get_phone(),
            type = await self.parse.creator_type(),
            listings = await self.parse.listing(),
            website_url = await self.parse.website_url(),
            on_kijiji_from = await self.parse.on_kijiji_from(),
            avg_reply = await self.parse.avg_reply(),
            reply_rate = await self.parse.reply_rate()
        )

        return user
    
    async def item_insert(self):
        item = dict(
            ad_id = await self.parse.ad_id(),
            title = await self.parse.title(),
            location = await self.parse.location(),
            address = await self.parse.address(),
            published_date = await self.parse.published_date(),
            price = await self.parse.price(),
            description = await self.parse.description()
        )

        return item

    async def overview_dict(self):
        hhw = await self.parse.hydro_heat_water()
        overview = dict(
            hydro = 'Yes: Hydro' in hhw,
            heat = 'Yes: Heat' in hhw,
            water = 'Yes: Water' in hhw,
            wifi = await self.parse.wifi(),
            parking = await self.parse.parking(),
            agreement_type = await self.parse.agreement_type(),
            move_in_date = await self.parse.move_in_date(),
            pet_friendly = await self.parse.pet_friendly()
        )

        return overview


    
    async def unit_dict(self):
        outdoor_spase = await self.parse.outdoor()
        units = dict(
            size = await self.parse.size(),
            furnished = await self.parse.furnished(),
            air_conditioning = await self.parse.air_condition(),
            balcony = 'Balcony' in outdoor_spase if outdoor_spase else False,
            yard = 'Yard' in outdoor_spase if outdoor_spase else False,
            smoking_permitted = await self.parse.smoking()
        )

        apps = await self.parse.appliances()
        if apps:
            apps_dict = dict(
                laundry_in_unit = apps[0],
                lundry_in_building = apps[1],
                dishwasher = apps[2],
                fridge = apps[3]
            )
            units.update(apps_dict)
        return units