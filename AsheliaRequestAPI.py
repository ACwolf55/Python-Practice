pip install requests
import requests

ashelia_get = requests.get('https://www.moogleapi.com/api/v1/characters/search?name=ashe')
ashelia = ashelia.json()

print(ashelia)
