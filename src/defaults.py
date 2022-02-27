import os

CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.join(CURRENT_FILE_DIR, '', '..')
TASK_DATA_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, 'ne-data.json')
UP_INTERFACE_CARDS_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, 'up_interfaces_cards.json')
LOG_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, 'parser')
