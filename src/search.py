import logging


logger = logging.getLogger(__name__)

def get_n(element_count, percent):
    return round(element_count * percent / 100)


def simple_search(polygon_data):
    logging.info('Start simple_search')
    res = []
    for group in polygon_data['data']:

        group['elements'].sort(key=lambda d: d['contour'].area, reverse=True)
        n = get_n(len(group['elements']), group['percent'])

        res.append([name['id'] for name in group['elements'][:n]])
    logging.info('Finish simple_search')
    return res
