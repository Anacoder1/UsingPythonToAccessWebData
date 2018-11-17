import urllib.request as ur
from bs4 import *

url = 'http://py4e-data.dr-chuck.net/known_by_Caroline.html'
curr_rep_count = 0
rep_count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while curr_rep_count < rep_count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == pos - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    curr_rep_count += 1
print('Last Url: ', url)