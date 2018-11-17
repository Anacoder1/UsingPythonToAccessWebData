import urllib.request as ur
import xml.etree.ElementTree as et

url = 'http://py4e-data.dr-chuck.net/comments_124120.xml'

total_num = 0
sum = 0

print('Retrieving - ', url)
xml = ur.urlopen(url).read()
print('Retrieved - ', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_num += 1

print('Count: ', total_num)
print('Sum: ', sum)