import json
import logging

from shapely.wkt import loads


logger = logging.getLogger(__name__)


def read(file_name):
    logger.info('Load data from ' + file_name)

    with open(file_name) as json_file:
        data = json.load(json_file)

    data['typical_defeat_combination']  # validation key in json
    data['object_id']  # validation key in json

    for group in data['data']:

        group['percent']  # validation key in json
        group['typical_element']  # validation key in json

        for item in group['elements']:

            item['id']  # validation key in json

            pol = item['contour']
            polyg = loads(pol.split(';')[1])

            item['contour'] = polyg
    logger.info('Data loaded')
    return data
