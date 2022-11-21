from bs4 import BeautifulSoup as BS
import re
from typing import Optional, List
from constants.web_data import reveal_phone_body, post_headers, post_url
import json
import httpx


class BS4Parse:

    def __init__(self, html, item_url) -> None:
        self.soup = BS(html, 'lxml')
        self.item_url = item_url


    async def health_check(self):
        return self.soup.find('div')


    async def hiden_phone(self):
        try:
            hiden = self.soup.find('span', class_='phoneNumberStart-404348366')
            return hiden
        except:
            return None



    async def creator_name(self) -> Optional[str]:
        try:
            url = await self.profile_url()
            name = url.split('/')[1][2:].replace('-', ' '). title()
            return name
        except:
            return None

    
    async def profile_url(self) -> Optional[str]:
        try:
            profile_url = self.soup.find('a', class_="link-2686609741").get('href')
            return profile_url
        except:
            return None


    async def get_phone(self):
        if await self.hiden_phone():
            try:
                prof_url = await self.profile_url()
                variables = dict(
                        adId=await self.ad_id(),
                        sellerId=prof_url.split('/')[2],
                        vipUrl=self.item_url,
                        listingType="rent",
                        sellerName=await self.creator_name()
                    )
                reveal_phone_body[0]['variables'] = variables
                data = json.dumps(reveal_phone_body)
                print('\n phonePostData', data, '\n\n')
                r = httpx.post(url=post_url, data=data, headers=post_headers)
                r = json.loads(r.text)
                print('\n phoneResponse', r, '\n\n')
                phone = r[0].get('data').get('getDynamicPhoneNumber').get('local')
            except Exception as ex:
                print('[ERROR] phone number: ', ex)
                phone = None
            return phone

    async def creator_type(self) -> Optional[str]:
        try:
            type = self.soup.find('div', class_='line-2791721720').get_text(strip=True)
            return type
        except:
            return None


    async def on_kijiji_from(self) -> Optional[str]:
        try:
            date = self.soup.find('div', {"data-qa-id": re.compile("member-since-stat")}).find(
                "span", class_="date-862429888"). get_text(strip=True)
            return date
        except:
            return None


    async def listing(self) -> Optional[int]:
        try:
            listing = self.soup.find('use', {"xlink:href": "#icon-listing"}).parent.parent.find("span").get_text()
            listing = int(listing)
            return listing
        except:
            return None


    async def website_url(self) -> Optional[str]:
        try:
            creator_block = self.soup.find_all("div", class_="line-2791721720")
            for item in creator_block:
                url = item.find('a', {"rel": "noopener noreferrer"})
                if url:
                    website_url = url.get('href')
                    return website_url
        except:
            return None

    
    async def avg_reply(self) -> Optional[int]:
        try:
            avg_reply = self.soup.find('div', {"data-qa-id": "responsiveness-stat-block"}).find(
                'div', class_='text-910784403').get_text(strip=True)
            return avg_reply
        except:
            return None

    
    async def reply_rate(self) -> Optional[str]:
        try:
            reply_rate = self.soup.find('div', {"data-qa-id": "reply-rate-stat-block"}).find(
                'div', class_='text-910784403').get_text(strip=True)
            return reply_rate
        except:
            return None
    
    

    async def ad_id(self) -> Optional[str]:
        try:
            ad_id = self.soup.find('li', class_='currentCrumb-3831268168').get_text(strip=True)
            return ad_id[5:]
        except:
            return None


    async def location(self) -> Optional[str]:
        try:
            location = self.soup.find('button', {"id": "SearchLocationPicker"}).get_text(strip=True)
            return location
        except:
            return None


    async def title(self) -> Optional[str]:
        try:
            title = self.soup.find_all('h1', class_='title-2323565163')[-1].get_text(strip=True)
            return title
        except:
            return None
            

    async def address(self) -> Optional[str]:
        try:
            address = self.soup.find(
                'div', class_='locationRow-2870378686').find(
                    'div', class_='locationContainer-2867112055').find(
                        'span', {"itemprop": "address"}).get_text(strip=True)
            return address
        except:
            return None

    
    async def published_date(self) -> Optional[str]: # we convert it into dateformat later
        try:
            time = self.soup.find('time').get('datetime')
            return time
        except:
            return None


    async def price(self) -> Optional[int]:
        try:
            price = self.soup.find('div', class_='priceWrapper-1165431705').find('span').get('content')[:-1]
            price = int(price)
            return price
        except:
            return None


    async def description(self) -> Optional[str]:
        try:
            description = self.soup.find('div', class_="root-2377010271 light-3420168793 card-745541139").get_text(strip=True)
            description.replace(r'\n', '')
            return description
        except:
            return None


    async def hydro_heat_water(self) -> List:  # returns example [None, 'Yes: Hydro', 'No: Heat', 'Yes: Water']
        try:           
            container = self.soup.find('svg', class_="icon-459822882 attributeGroupIcon-3454750106").parent.find_all('svg')
            utilits = [x.get('aria-label') for x in container]
            return utilits
        except:
            return []


    async def wifi(self) -> bool:
        try:
            wifi = self.soup.find('use', {"xlink:href": "#icon-attribute-group-wifiandmore"}).parent.parent.get_text()
            wifi = 'Included' in wifi and 'Not Included' not in wifi
            return wifi
        except:
            return False

       
    async def parking(self) -> bool:
        try:
            parking = self.soup.find('use', {"xlink:href": "#icon-attributes-numberparkingspots"}).parent.parent.get_text().replace('Parking Included', '')
            parking = int(parking)
            return parking
        except:
            return 0
  
    async def agreement_type(self) -> Optional[str]:
        try:
            agr_type = self.soup.find('use', {"xlink:href": "#icon-attributes-agreementtype"}).parent.parent.get_text().replace('Agreement Type', '')
            return agr_type
        except:
            return None

            
    async def move_in_date(self) -> Optional[str]:
        try:
            date = self.soup.find('use', {"xlink:href": "#icon-attributes-dateavailable"}).parent.parent.get_text().replace('Move-In Date', '')
            return date
        except:
            return None


    async def pet_friendly(self) -> Optional[str]: # ('Yes', 'No', 'Limited')
        try:
            pet = self.soup.find('use', {"xlink:href": "#icon-attributes-petsallowed"}).parent.parent.get_text().replace('Pet Friendly', '')
            return pet
        except:
            return None


    async def size(self) -> Optional[int]:
        try:
            size = self.soup.find('use', {"xlink:href": "#icon-attributes-areainfeet"}).parent.parent
            size = int(size.find('dd', class_='twoLinesValue-2815147826').get_text().replace(',', ''))
            return size
        except:
            return None
    

    async def furnished(self) -> bool:
        try:
            furnished = self.soup.find('use', {"xlink:href": "#icon-attributes-furnished"}).parent.parent.find(
                'dd', 'twoLinesValue-2815147826').get_text()
            furnished = 'Yes' in furnished
            return furnished
        except:
            return False


    async def appliances(self) -> List: # return example [True, False, False, True] or []
        try: 
            appliances_block = self.soup.find('use', {"xlink:href": "#icon-attribute-group-appliances"}).parent.parent
            all_appliances = appliances_block.find('ul', 'list-1757374920 disablePadding-1318173106').get_text(strip=True)
            result = list()
            result.append('Laundry (In Unit)' in all_appliances)
            result.append('Laundry (In Building)' in all_appliances)
            result.append('Dishwasher' in all_appliances)
            result.append('Fridge / Freezer' in all_appliances)
            return result
        except:
            return []


    async def air_condition(self) -> bool:
        try:
            air_condition = self.soup.find('use', {"xlink:href": "#icon-attributes-airconditioning"}).parent.parent.find(
                'dd', class_='twoLinesValue-2815147826').get_text()
            air_condition = 'Yes' in air_condition
            return air_condition
        except:
            return False


    async def outdoor(self) -> Optional[str]:
        try:
            outdoor = self.soup.find('use', {"xlink:href": "#icon-attribute-group-outdoorspace"}).parent.parent.find(
                'ul', 'list-1757374920 disablePadding-1318173106').get_text(strip=True)
            return outdoor
        except:
            return None

    
    async def smoking(self) -> bool:
        try:
            smoke = self.soup.find('use', {"xlink:href": "#icon-attributes-smokingpermitted"}).parent.parent.find(
                'dd', class_='twoLinesValue-2815147826').get_text()
            smoke = 'Yes' in smoke
            return smoke
        except:
            return False