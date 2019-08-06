from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'5',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '26fdf62c-4996-4e9b-b1dd-e8af3faf4bcc'
}

session = Session()
session.headers.update(headers)
requrl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=26fdf62c-4996-4e9b-b1dd-e8af3faf4bcc'




try:
    response = requests.get(requrl)
    data = json.loads(response.text)
    content = json.loads(response.content)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


# print(json.dumps(data['data'][0], indent=4))
# print(len(data['data']))

my_coins = ['BTC','ETH','BCH']

portfolio = [
    {
        'symbol':'BTC',
        'amount_owned': 2,
        'price_per_coin': 3200
    },
    {
        'symbol':'ETH',
        'amount_owned': 100,
        'price_per_coin': 2.05
    }
]
print(len(portfolio))
for i in range(len(data['data'])):
    if data['data'][i]['symbol'] in [portfolio[i]['symbol'] for i in range(len(portfolio))]:
        print(data['data'][i]['symbol'])
        print('{0:.2f}'.format(data['data'][i]['quote']['USD']['price']))
        print('============================')




