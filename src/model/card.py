class Card:

    def __init__(self, name, interfaces):
        self.name = name
        self.interfaces = interfaces

    def __str__(self) -> str:
        string = self.name + '\n'
        for interface in self.interfaces:
            string = string + '\t{} {} {} \n'.format(interface.name, interface.status, interface.id)
        return string


