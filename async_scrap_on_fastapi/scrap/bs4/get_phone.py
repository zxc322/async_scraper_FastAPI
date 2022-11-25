import json
import httpx

from constants.web_data import post_headers


async def pnone_by_post_method(data: list):
    try:
        print(f'--- phone by post ---')
        data = json.dumps(data)
        r = httpx.post(url="https://www.kijiji.ca/anvil/api", data=data, headers=post_headers)
        r = json.loads(r.text)
        phone = r[0].get('data').get('getDynamicPhoneNumber').get('local')
    except:
        phone = None
    print(f'phone: {phone}')
    return phone


async def phone_by_token(token: str):
    try:
        print(f'--- phone by token {token} ---')
        url = "https://www.kijiji.ca/j-vac-phone-get.json"
        params = {"token": token}
        r = httpx.get(url=url, headers=post_headers, params=params)
        response = json.loads(r.text)
        phone = response.get('phone')
    except:
        phone = None
    print(f'phone: {phone}')
    return phone
    

