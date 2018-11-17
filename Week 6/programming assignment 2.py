import urllib.request as ur
import urllib.parse as up
import json

apiEndpoint = 'http://py4e-data.dr-chuck.net/geojson?'

addr_input = input('Enter location: ')
params = {'sensor' : 'false', 'address' : addr_input}
url = apiEndpoint + up.urlencode(params)
print('Retrieving - ', url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved - ', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj['results'][0]['place_id']
print('Place id', place_id)

