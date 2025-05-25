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
table = soup.findAll('ul')

logbooks = []
for book in table:
    li = book.next
    if li.name == "li":
        a = li.next
        if a.name == "a":
            logbook_url = a.attrs.get("href", None)
            if logbook_url:
                logbooks.append(logbook_url)

print(logbooks)