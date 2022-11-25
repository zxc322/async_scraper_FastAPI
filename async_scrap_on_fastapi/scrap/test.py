# import httpx, time, json
# from bs4 import BeautifulSoup as BS

# urls = list()

# f = open('urls.txt', 'r')


# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
# }

# def seeker(spltd: list):
#     for el in spltd:
#         if 'phoneToken' in el:
#             token = json.loads(el.replace('"phoneToken":', ''))
#             return token

# i = 1
# for url in f:
#     r = httpx.get(url=url[:-1], headers=headers)

    
#     s = BS(r.text, 'lxml')
#     scripts = s.find('div', {'id': 'FesLoader'})
#     if scripts:
#         script = scripts.script.get_text()
#         spltd = script.split(',')
#         token = seeker(spltd)
#         print(f'page-{i}, url: {url}\ntoken: {token}\n')

#         i += 1
#         # if i>10:
#         #     break




# f.close()

try:
    try:
        print(1+'1')
    except:
        print('2+2')
except:
    print('3+3')