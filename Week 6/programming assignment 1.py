import urllib.request as ur
import json

json_url = 'http://py4e-data.dr-chuck.net/comments_124121.json'
print("Retrieving - ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved -', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_num = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_num += 1

print('Count:', total_num)
print('Sum:', sum)