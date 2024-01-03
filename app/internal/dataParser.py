import json
# tested on page 1, 2 and 3
key_set = ['srm', 'style', 'labels',
           'glass', 'available', 'beerVariation']
# temporarily added will remove later
DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/api'


def parseDictToJsonString(Modler, data_json):
    dataModelList = []
    for item in data_json['data']:
        for key in key_set:
            if key in item.keys():
                item[key] = json.dumps(item[key])
        dataModelList.append(Modler(**item))
    return dataModelList
