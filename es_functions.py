import requests
import json
from pprint import pprint


def create_report(data):
    url = 'http://localhost:9200/reports/report/'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    return json.loads(r.text)

def get_all_datasets():
    search_obj = {
            "size": 0,
            "aggs" : {
                "langs" : {
                    "terms" : { "field" : "chart.data.url.keyword"}
                }
            }
        }

    url = 'http://localhost:9200/_search'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(search_obj), headers=headers)

    return r.text

def get_all_charts():
    # url = 'http://localhost:9200/reports/_search'

    # headers = {'content-type': 'application/json'}

    # r = requests.get(url, headers=headers)

    # return json.loads(r.text)

    search_obj = {
            "size": 0,
            "aggs" : {
                "chart_types" : {
                    "terms" : { 
                        "field" : "chart.type.keyword"
                    }
                },
                "chart_ids" : {
                    "terms" : { 
                        "field" : "chart._id"
                    }
                }
            }
        }
    

    url = 'http://localhost:9200/_search'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(search_obj), headers=headers)

    return r.text

def get_reports_by_tag(tag):
    search_obj = {
        "query": {
            "query_string": {
                "query": tag,
                "fields": ['tags']
            }
        }
    }

    url = 'http://localhost:9200/_search'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(search_obj), headers=headers)

    return r.text

def get_all_reports():
    
    url = 'http://localhost:9200/reports/report/_search'

    headers = {'content-type': 'application/json'}

    r = requests.get(url, headers=headers)

    return r.text

def update_mapping(obj, field):
    map_obj = {
        "properties": {
            field : {
            "type": "text",
            "fielddata": True
            }
        }
    }

    url = 'http://localhost:9200/reports/_mapping/my_type?update_all_types'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(map_obj), headers=headers)

    return r.text