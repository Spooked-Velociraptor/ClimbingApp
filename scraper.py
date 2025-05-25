from bs4 import BeautifulSoup

import json
import requests

# Headers to mimic the browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

books = requests.get('https://www.ukclimbing.com/logbook/books/#c1', headers)


soup = BeautifulSoup(books.content, "html.parser")
table = soup.findAll('ul')

values = list(filter(None, table[0].text.split('\n')))
values = list(filter(None, [value.replace("\xa0", "") for value in values[1:]]))

d = {}
for item in values:
    key, value = item.split('.', maxsplit=1)
    d[key] = value

#print(x.text)