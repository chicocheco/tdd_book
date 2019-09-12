from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Tania jde na domovskou stranku a omylem zkusi na seznam pridat prazdny text.
        # Stiskne Enter na vstupnim datovem poli.

        # Domovska stranska se obnovi a objevi se chyba rikajici ze pridavane polozky nesmi byt prazdne

        # Nyni to zkusi znovu s nejakym textem pro polozku, coz funguje

        # Skodolibe, ted zkusi znovu pridat druhou prazdnou polozku

        # Dostane podobne varovani na strance seznamu

        # Ted to muze opravit vyplnenim pole nejakym textem
        self.fail('write me!')
