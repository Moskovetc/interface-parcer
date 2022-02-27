INTERFACE_ID_FIELD_NAME = 'id'
INTERFACE_NAME_FIELD_NAME = 'name'
INTERFACE_ADMIN_STATUS_FIELD_NAME = 'admin-status'
INTERFACE_ADMIN_STATUS_UP = 'up'
INTERFACE_LOCATION = 'hw-component-reference-ref-name'
INTERFACE_VIRTUAL_LOCATION_NAME = 'virtual'


class Interface:

    def __init__(self, interface_data):
        self.id = interface_data[INTERFACE_ID_FIELD_NAME]
        self.name = interface_data[INTERFACE_NAME_FIELD_NAME]
        self.status = interface_data[INTERFACE_ADMIN_STATUS_FIELD_NAME]
        self.location = self.get_interface_location(interface_data)

    def is_up_admin_status(self):
        return self.status == INTERFACE_ADMIN_STATUS_UP

    def is_virtual(self):
        return self.location == INTERFACE_VIRTUAL_LOCATION_NAME

    @staticmethod
    def get_interface_location(interface_data):
        if INTERFACE_LOCATION in interface_data:
            return interface_data[INTERFACE_LOCATION]
        return INTERFACE_VIRTUAL_LOCATION_NAME
