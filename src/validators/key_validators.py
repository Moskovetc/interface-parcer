from validators.exceptions import InvalidInterfaceStructure


class KeyValidator:

    def validate(self, key, interface):
        if key not in interface:
            raise InvalidInterfaceStructure('Invalid interface structure, key with name {} is not exist'.format(key))
