import urllib.request as ur
from bs4 import *

html = ur.urlopen('http://py4e-data.dr-chuck.net/comments_124118.html').read()
soup = BeautifulSoup(html, 'html.parser')

span_count = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    span_count += 1

print('Count ', span_count)
print('Sum ', sum)