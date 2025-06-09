from bs4 import BeautifulSoup
import requests
import lxml
import re
from climb_detail import grade_list

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = "https://www.ukclimbing.com"
book_page = requests.get('https://www.ukclimbing.com/logbook/books/#c1', headers)

soup = BeautifulSoup(book_page.content, "html.parser")

book_html = soup.find(id = 'c1')
tag_types = ["a"]

def convert_grade(x):
    try:
        v = grade_list[int(x)]
    except:
        v = 'Unknown'
    return v

def find_crags(x):
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    crag_link = soup.find('table')

    if crag_link:
        for tag in crag_link.find_all(tag_type):
            names = tag.attrs.get('href')
            if names:
                with open("crag names.txt", "a") as f:
                    f.writelines(names + '\n')

def climbs(y, z):
    soup = BeautifulSoup(requests.get(y).content, 'lxml')
    scripts = soup.find_all('script')

    for script in scripts:
        if script.string is not None:
            if script.string.strip().startswith('let cragId ='):
                # find table data (list of climbs & info)
                a = script.string.strip()

                c = a.split('table_data =')[1] # remove everything before 'table_data'
                c = c.split('grade_type_list')[0] # remove everything after 'grade_type_list'
                c = c.lstrip(' [').rstrip('],\n\t\t\t\t')
                
                tokens = re.split(r"[:,{}]", c)

                for i in range(len(tokens)):
                    if tokens[i] == '"name"':
                        name = tokens[i+1].strip('""')
                        grade = tokens[i+3].strip('""')
                        igrade = convert_grade(grade)
                        print(igrade)
                        link = tokens[i+27].strip('""')
                        base_link = z
                        with open("climb names.txt", "a") as f:
                            f.write(base_link + '|' + name + '|' + igrade + '|/' + link + '\n')
        
for tag_type in tag_types:
    for tag in book_html.find_all(tag_type):
        logbook = tag.attrs.get('href')
        if logbook:
            full_link = 'https://www.ukclimbing.com' + logbook
        
with open("crag names.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        climb_full_link = base_url + l.strip('\n')
        climbs(climb_full_link, l.strip())