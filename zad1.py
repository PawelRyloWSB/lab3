import logging


def log(level, message):
    logging.basicConfig(filename='logs.log', encoding='utf-8', level=level,
                        format='%(asctime)s: level: %(levelname)s - functionName: %(funcName)s - message: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

    match level:
        case logging.CRITICAL:
            logging.critical(message)
        case logging.ERROR:
            logging.error(message)
        case logging.WARNING:
            logging.warning(message)
        case logging.INFO:
            logging.info(message)
        case logging.DEBUG:
            logging.debug(message)


log(logging.ERROR, 'Example message')
