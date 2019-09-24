from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Tania jde na domovskou stranku a omylem zkusi na seznam pridat prazdny text.
        # Stiskne Enter na vstupnim datovem poli.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Domovska stranska se obnovi a objevi se chyba rikajici ze pridavane polozky nesmi byt prazdne
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item."
        ))
        # lambda makes possible saving the assertEqual func as an argument to work with later,
        # not executing it immediately and therefore just once

        # Nyni to zkusi znovu s nejakym textem pro polozku, coz funguje
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Skodolibe, ted zkusi znovu pridat druhou prazdnou polozku
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Dostane podobne varovani na strance seznamu
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item."
        ))

        # Ted to muze opravit vyplnenim pole nejakym textem
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

        # self.fail('Finish this test!')
