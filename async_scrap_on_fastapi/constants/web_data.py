LOCATIONS = {
    1: ('b-apartments-condos/city-of-toronto', 'c37l1700273'),
    2: ('b-immobilier/ville-de-quebec', 'c34l1700124'),
    3: ('b-apartments-condos/nova-scotia', 'c37l9002'), 
    4: ('b-apartments-condos/new-brunswick', 'c37l9005'), 
    5: ('b-apartments-condos/manitoba', 'c37l9006'),
    6: ('b-apartments-condos/british-columbia', 'c37l9007'),
    7: ('b-apartments-condos/prince-edward-island', 'c37l9011'),
    8: ('b-apartments-condos/saskatchewan', 'c34l9009'),
    9: ('b-apartments-condos/alberta', 'c37l9003'),
    10: ('b-apartments-condos/newfoundland', 'c37l9008'),
    'all': 'Get all regions'
}
    
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'connection': 'keep-alive',

}

post_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8', 'connection': 'keep-alive', 'host': 'www.kijiji.ca',
    'Content-Type': 'application/json'
    }
    
post_url = 'https://www.kijiji.ca/anvil/api'

reveal_phone_body = [
    {"operationName":"GetDynamicPhoneNumber",
    "variables":{
        "adId":"1638825913",
        "sellerId":"1025982268",
        "vipUrl":"https://www.kijiji.ca/v-apartments-condos/city-of-toronto/1br-2br-brand-new-condo-units-available-at-yonge-lakeshore/1638825913?siteLocale=en_CA",
        "listingType":"rent",
        "sellerName":"Prestige - Pinnacle One Yonge"
        },
    "query":"query GetDynamicPhoneNumber($sellerId: String!, $adId: String!, $userId: String, $vipUrl: String!, $listingType: String!, $sellerName: String!) {\n  getDynamicPhoneNumber(sellerId: $sellerId, adId: $adId, userId: $userId, vipUrl: $vipUrl, listingType: $listingType, sellerName: $sellerName) {\n    local\n    e164\n    __typename\n  }\n}\n"}]
       
params = {
    'token': '1505729653:ABUu7Z6DSR9OtVA4TQ61SAQKOV_KwqZL/hzhD/nu7fE-'
}