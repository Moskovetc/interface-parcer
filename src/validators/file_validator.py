from validators.exceptions import InvalidFileStructure
from validators.interface_validators import InterfaceValidator


class FileValidator:

    def validate(self, data):
        validator = InterfaceValidator()
        try:
            interfaces = data['task_result']['content']['network-element'][0]['interface']
        except BaseException as exception:
            raise InvalidFileStructure('File structure is invalid, could not get interfaces', exception)
        for interface in interfaces:
            validator.validate(interface)
