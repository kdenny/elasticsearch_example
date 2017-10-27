import requests
import json
from pprint import pprint


class Reports:
    url = 'http://localhost:9200/reports/report/'
    headers = {'content-type': 'application/json'}

    def create(self, data):
        r = requests.post(self.url, data=json.dumps(data), headers=self.headers)

        return json.loads(r.text)