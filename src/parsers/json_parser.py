import re

from logger.log_config import log
from model.card import Card

BRAND_REGULAR_EXPRESSION = r"^\w+"


class JsonParser:
    """
        JSON Parser class
    """

    @log
    def parse(self, interfaces):
        interface_dict = self._filter_interfaces(interfaces)
        cards = self._get_cards(interface_dict)
        return cards

    def _filter_interfaces(self, interfaces):
        interface_dict = {}
        for interface in interfaces:
            if interface.is_up_admin_status():
                name = self._get_card_name(interface)
                if name in interface_dict:
                    interface_dict[name].append(interface)
                else:
                    interface_dict[name] = [interface]
        return interface_dict

    def _get_card_name(self, interface):
        if interface.is_virtual():
            return interface.location
        brand_name = str(re.findall(BRAND_REGULAR_EXPRESSION, interface.name)[0])
        name = '{}-{}'.format(interface.location, brand_name)
        return name

    def _get_cards(self, interface_dict):
        cards = []
        for key, value in interface_dict.items():
            card = Card(key, value)
            cards.append(card)
        return cards
