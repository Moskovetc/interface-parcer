from validators.key_validators import KeyValidator


class InterfaceValidator:

    def validate(self, interface):
        key_validator = KeyValidator()
        key_validator.validate('admin-status', interface)
        key_validator.validate('name', interface)
