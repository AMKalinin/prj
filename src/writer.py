import json
import logging


logger = logging.getLogger(__name__)


def write_result(
        file_name,
        combination,
        object_id,
        data=None,
        error_message=None):

    logger.info('Creating output files in ' + file_name)
    with open(file_name, 'w') as file:
        out_dict = {
            'typical_defeat_combination': combination,
            'object_id': object_id,
        }
        if error_message:
            out_dict['result'] = False
            out_dict['message'] = error_message
            json.dump(out_dict, file, ensure_ascii=False)
        else:
            out_dict['result'] = True
            out_dict['message'] = ''
            out_dict['data'] = data
            json.dump(out_dict, file, ensure_ascii=False)
    logger.info('Output file created')
