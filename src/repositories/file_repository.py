import json
import os

from logger.log_config import log
from model.interface import Interface
from model.network_element import NetworkElement
from validators.file_validator import FileValidator

TASK_RESULT_FIELD_NAME = 'task_result'
CONTENT_FIELD_NAME = 'content'
NETWORK_ELEMENT_FIELD_NAME = 'network-element'
NETWORK_ELEMENT_NAME_FIELD_NAME = 'name'
INTERFACE_FIELD_NAME = 'interface'
READ_ACCESS = 'r'
APPEND_ACCESS = 'a'


class FileRepository:
    """
        File repository provides
        load from file
        save methods to file
        load interfaces from file
    """

    @log
    def load_network_elements(self, path):
        data = self.load(path)
        network_elements_data = data[TASK_RESULT_FIELD_NAME][CONTENT_FIELD_NAME][NETWORK_ELEMENT_FIELD_NAME]
        network_elements = []
        for network_element in network_elements_data:
            interfaces = []
            for interface in network_element[INTERFACE_FIELD_NAME]:
                interfaces.append(Interface(interface))
            network_element_name = network_element[NETWORK_ELEMENT_NAME_FIELD_NAME]
            network_elements.append(NetworkElement(network_element_name, interfaces))
        return network_elements

    @log
    def load(self, path):
        with open(path, READ_ACCESS) as file:
            data = json.load(file)
        self._validate_source(data)
        return data

    @log
    def save(self, save_path, data):
        with open(save_path, APPEND_ACCESS) as file:
            for card in data:
                file.write(str(card))

    @log
    def delete_file(self, save_path):
        try:
            os.remove(save_path)
        except OSError:
            pass

    def _validate_source(self, data):
        file_validator = FileValidator()
        file_validator.validate(data)
