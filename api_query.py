import requests
import json


url = 'http://localhost:9200/movies/movie/1'

headers = {'content-type': 'application/json'}


r = requests.get(url, headers=headers)

print(r.text)

# r = requests.delete(url, headers=headers)

# print(r.text)


