import argparse
import logging

import reader
import search
import writer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info('Started')

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', '-i', type=str, help='Входной файл')
    parser.add_argument('--output_file', '-o', type=str, help='Выходной файл')
    namespace = parser.parse_args()

    data = None
    combination = None
    object_id = None

    try:
        data = reader.read(namespace.input_file)
        combination = data['typical_defeat_combination']
        object_id = data['object_id']
    except KeyError as err:
        error_message = 'Ошибка в структуре входного файла. Отсутствует поле ' + str(err) + '.'
        logger.error(error_message)
    except FileNotFoundError:
        error_message = 'Входной файл не найден.'
        logger.error(error_message)

    if data:
        result = search.simple_search(data)

    try:
        if data:
            writer.write_result(namespace.output_file,
                                combination,
                                object_id,
                                data=result)
        else:
            writer.write_result(namespace.output_file,
                                combination,
                                object_id,
                                error_message=error_message)
    except FileNotFoundError:
        logger.error('Данный каталог отсутствует.')

    logger.info('Finished')


if __name__ == "__main__":
    main()
