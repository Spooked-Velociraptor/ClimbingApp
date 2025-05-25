from bs4 import BeautifulSoup

import json
import requests

# Headers to mimic the browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

book_page = requests.get('https://www.ukclimbing.com/logbook/books/#c1', headers)


soup = BeautifulSoup(book_page.content, "html.parser")

book_html = soup.find(id = 'c1')

tag_types = ["p", "ul", "li", "a"]

for tag_type in tag_types:
    for tag in book_html.find_all(tag_type):
        print(tag.attrs.get('href'))