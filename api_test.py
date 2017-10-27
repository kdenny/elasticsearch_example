import requests
import json
from pprint import pprint
from es_functions import *

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

