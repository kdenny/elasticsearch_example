import requests
import json
from pprint import pprint


def add_object(data):
    url = 'http://localhost:9200/reports/report/'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r.text

def get_objects():
    url = 'http://localhost:9200/reports/_search'

    headers = {'content-type': 'application/json'}

    r = requests.get(url, headers=headers)

    return json.loads(r.text)




def search_query(qstring, fields):
    if qstring != '':
        search_obj = {
            "query": {
                "query_string": {
                    "query": qstring,
                    "fields": fields
                }
            }
        }
    else:
        search_obj = {
            "_source": ["chart.data.id", "chart.data.url"],
            # "query": {
            #     "exists" : { "field" : "chart.data" }
            # },
            "size": 0,
            "aggs" : {
                "langs" : {
                    "terms" : { "field" : "chart.data.id"}
                }
            }
        }

    url = 'http://localhost:9200/_search'

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(search_obj), headers=headers)

    pprint(json.loads(r.text))

def get_index_length(ind_name):
    url = 'http://localhost:9200/{0}/_search'.format(ind_name)

    headers = {'content-type': 'application/json'}

    r = requests.get(url, headers=headers)

    all_res = json.loads(r.text)['hits']['total']
    print(all_res)











reports_list = [{
    "title": "Pageviews by DMA",
    "description": "Bar Chart for a small subset of DMAs",
    "layout": {'row_1': {'id': 1,
        'width': 900,
        'height': 550}
    },
    "chart": [{
        'type': 'line',
        'data': {
            'id': 2,
            'name': 'Publisher Benchmarking',
            'url': 'http://nimbuscharts.pythonanywhere.com/sheets/13eU1yFNUO6guspeQRFRiVPugp0Ihrjym8BSXnKL6Ukw/Sheet1/',
            'fields': ['DMA Name', 'Conversions'],
            'publisher_id': 'o19WonOrHQ'
        },
        'render_schema': {
            'xVar': 'DMA Name',
            'yVar': 'Conversions',
            'xLabel': 'DMA Name',
            'yLabel': 'Conversions',
        }
    }],
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
    
}]

# for report in reports_list:

#     b = json.loads(add_object(report))
#     pprint(b)

# a = get_objects()
# pprint(a['hits'])

# get_index_length('reports')

# query = '2'
# # query = ''
# fields = ['chart.data.id']

# search_query(query, fields)


a = {'df': 12}
from elasticsearch_api import Reports

report_api = Reports()

report_api.create(data=a)