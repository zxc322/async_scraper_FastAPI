class MultiFilter:

    def __init__(self, filters: dict, order_by: tuple, limit: int, offset: int) -> None:
        self.filters = filters
        self.order_by = order_by
        self.limit = limit
        self.offset = offset
        

    def retrieve_item(self):
        query = "SELECT\
            ad_id,\
            title,\
            location,\
            address,\
            published_date,\
            price,\
            description,\
            creator_id,\
            name as creator_name,\
            profile_url as creator_profile,\
            phone,\
            type as creator_type,\
            listings as creators_total_listings,\
            on_kijiji_from,\
            avg_reply,\
            reply_rate,\
            hydro, heat, water, wifi, parking,\
            agreement_type,\
            move_in_date,\
            pet_friendly,\
            size, furnished, laundry_in_unit,\
            lundry_in_building,\
            dishwasher, fridge,\
            air_conditioning, balcony, yard, smoking_permitted \
            FROM items\
            JOIN users\
            ON items.creator_id = users.user_id\
            JOIN overview\
            ON items.item_id = overview.item_id\
            JOIN unit\
            ON items.item_id = unit.item_id"

        query += self.__generate_filters()
        query += self.__order_by_seq()
        query += ' LIMIT {} OFFSET {}'.format(self.limit, self.offset)
        return query


    def get_count(self):
        query = "SELECT COUNT(*) as total_items\
            FROM items\
            JOIN users\
            ON items.creator_id = users.user_id\
            JOIN overview\
            ON items.item_id = overview.item_id\
            JOIN unit\
            ON items.item_id = unit.item_id"

        query += self.__generate_filters()
        return query


    def __generate_filters(self):
        where = " WHERE items.item_id IS NOT NULL"
        for k, v in self.filters.items():
            if isinstance(v, list):
                where += f" AND {k} BETWEEN '{str(v[0])}' AND '{str(v[1])}'"
            else:
                where += f" AND {k} = '{str(v)}'" 
        return where

    def __order_by_seq(self):
        if self.order_by:
            res = ' ORDER BY'
            for el in self.order_by:
                res += f' {el},'
            return res[:-1]


