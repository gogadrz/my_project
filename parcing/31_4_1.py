import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3/')

data = json.loads(my_req.text)  # десериализация json

data['name'] = 'gogadrz'
data['height'] = 175
data['mass'] = 74
# print(json.dumps(data, indent=4))

with open('my_test.json', 'w') as file:
    json.dump(data, file,
              indent = 4)
# print('*' * 80)
#
# print(my_req.url)

req_url = requests.get('https://swapi.dev/api/people/3/')

deser_url = json.loads(req_url.text)
# my_dict = json.dumps(deser_url, indent = 4)
# print(my_dict['films'])
# print(json.dumps(deser_url, indent = 4))
print(deser_url['films'])
