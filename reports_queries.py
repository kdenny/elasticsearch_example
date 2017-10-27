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














new_dataset = {
        'id': 5,
        'name': 'More Random Data',
        'url': 'http://nimbuscharts.pythonanywhere.com/sheets/13eU1yFNUO6guspeQRFRiVPugp0Ihrjym8BSXnKL6Ukw/Sheet1/',
        'fields': ['DMA Name', 'Conversions'],
        'publisher_id': 'o19WonOrHQ'
    }

new_chart = {
    'id': 'XTy34v',
    'type': 'line',
    'data': new_dataset,
    'render_schema': {
        'xVar': 'DMA Name',
        'yVar': 'Conversions',
        'xLabel': 'DMA Name',
        'yLabel': 'Conversions',
    },
    'properties': {
        'type': {
            "type": "text",
            "fielddata": True
        },
        'data': {
            "type": "nested"
        },
        'renderSchema': {
            "type": "nested"
        }
    }
}

new_report = {
    "title": "Pageviews by DMA",
    "description": "Bar Chart for a small subset of DMAs",
    "layout": {'row_1': {'id': 1,
        'width': 900,
        'height': 550}
    },
    "chart": [new_chart],
    "properties":{
      "title" : {
        "type" : "string"
      },
      "description":{
        "type" : "string"
      },
      "layout":{
        "type" : "nested"
      },
      "chart":{
        "type" : "nested"
      }
    }
}

# bt = create_report(new_report)
# print(bt)

# a = json.loads(get_all_datasets())


# charts = json.loads(get_all_charts())
# pprint(charts)

# b = update_mapping('report','chart.type')
# pprint(b)

a = get_all_reports()
pprint(json.loads(a))