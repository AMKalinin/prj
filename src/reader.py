import json
# from shapely.geometry import Polygon
from shapely.wkt import loads


def read2(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    res_data = []
    for group in data['data']:
        dict_info = {'percent': group['percent'],
                     'elements': []}

        for item in group['elements']:

            pol = item['contour']
            polyg = loads(pol.split(';')[1])

            dict_info['elements'].append({'id': item['id'], 'contour': polyg})
        res_data.append(dict_info)

    return res_data


def read(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

    for group in data['data']:
        for item in group['elements']:

            pol = item['contour']
            polyg = loads(pol.split(';')[1])
            print(item['id'], polyg.area)
            item['contour'] = polyg
        print()
    return data


if __name__ == '__main__':
    read('tdc/input_2.json')
