import logging
import time

from defaults import LOG_FILE_PATH

LOG_FILE_NAME = '{}_{}.log'.format(LOG_FILE_PATH, time.strftime('%d_%m_%y', time.localtime()))
LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s.%(funcName)s %(message)s"
LOG_FILE_ACCESS = 'a'

logging.basicConfig(
    filename=LOG_FILE_NAME,
    format=LOG_FORMAT,
    level=logging.DEBUG
)


def log(func):
    """
    :param func:
    :return wrapper: wrapper writes the called function name and args
    """
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        with open(LOG_FILE_NAME, LOG_FILE_ACCESS) as file:
            file.write('{} function {} start '.format(time.ctime(), func_str))
            file.write(' with args {}\n'.format(str(args)))
        return func(*args, **kwargs)

    return wrapper
