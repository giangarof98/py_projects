import requests

# specify address here
address = '157.240.22.35'

res = requests.get(f'http://ip-api.com/json/{address}')
data = res.json()

print(data)