import requests

ashe_get = requests.get('https://www.moogleapi.com/api/v1/characters/search?name=ashe')
ashelia = ashe_get.json()[0]

print(ashelia)