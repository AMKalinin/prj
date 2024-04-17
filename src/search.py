import math

import reader


def simple_search(polygon_data):
    for group in polygon_data['data']:
        group['elements'].sort(key=lambda d: d['contour'].area, reverse=True)

        n = len(group['elements']) * group['percent'] / 100
        print(math.ceil(n))

    return 0


if __name__ == '__main__':
    data = reader.read('tdc/input_4.json')
    simple_search(data)

    # a = [{'id': 1, 'value': 1.2},
    #      {'id': 2, 'value': 1.23},
    #      {'id': 3, 'value': 1.3},
    #      {'id': 4, 'value': 1.33},
    #      {'id': 5, 'value': 1.3},
    #      {'id': 6, 'value': 1.4},
    #      {'id': 7, 'value': 1}]
    # a.sort(key=lambda d: d['value'],)
    # print(a)
