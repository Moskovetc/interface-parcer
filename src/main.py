from defaults import TASK_DATA_FILE_PATH, UP_INTERFACE_CARDS_FILE_PATH
from parsers.json_parser import JsonParser
from repositories.file_repository import FileRepository

if __name__ == '__main__':
    repository = FileRepository()
    network_elements = repository.load_network_elements(TASK_DATA_FILE_PATH)
    parser = JsonParser()
    repository.delete_file(UP_INTERFACE_CARDS_FILE_PATH)
    for network_element in network_elements:
        cards = parser.parse(network_element.interfaces)
        repository.save(UP_INTERFACE_CARDS_FILE_PATH, cards)
