import urllib.request
from bs4 import BeautifulSoup
import requests
import lxml

# Headers to mimic the browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = "https://www.ukclimbing.com"
book_page = requests.get('https://www.ukclimbing.com/logbook/books/#c1', headers)

soup = BeautifulSoup(book_page.content, "html.parser")

book_html = soup.find(id = 'c1')

tag_types = ["a"]

def find_crags(x):
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    crag_link = soup.find('table')

    if crag_link:
        for tag in crag_link.find_all(tag_type):
            names = tag.attrs.get('href')
            if names:
                with open("crag names.txt", "a") as f:
                    f.writelines(names + '\n')

def climbs(y):
    soup = BeautifulSoup(requests.get(y).content, 'lxml')
    table = soup.find('table', id='climb_table')
    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        rows = []
        for row in table.tbody.find_all('tr'):
            cells = row.find_all('a')  
            # cells = [tr.text.strip() for tr in row.find_all('td')]
            rows.append(cells)
        # log data
        print("Headers:", headers)
        print("table_body:")
        for row in rows:
            print(row)

for tag_type in tag_types:
    for tag in book_html.find_all(tag_type):
        logbook = tag.attrs.get('href')
        if logbook:
            full_link = 'https://www.ukclimbing.com' + logbook
            # find_crags(full_link)
        
with open("crag names.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        climb_full_link = base_url + l.strip('\n')
        climbs(climb_full_link)