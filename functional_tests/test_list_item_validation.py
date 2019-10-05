from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Tania jde na domovskou stranku a omylem zkusi na seznam pridat prazdny text.
        # Stiskne Enter na vstupnim datovem poli.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # prohlizec zasahne do pozadavku a nenahraje list stranku
        # we check for the CSS pseudoselector :invalid, which browser applies to any HTML5 input that has invalid input
        # fallback: if the browser like Safari, does not fully implement HTML5, the custom error message will get used
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))
        # lambda makes possible saving the assertEqual func as an argument to work with later,
        # not executing it immediately and therefore just once

        # Nyni to zkusi znovu s nejakym textem pro polozku, coz funguje, chyba zmizi
        # when valid inputs when use the CSS pseudoselector :valid
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))

        # a muze bez problemu potvrdit predmet
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Skodolibe, ted zkusi znovu pridat druhou prazdnou polozku (jiz pro existujici list)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Dostane podobne varovani na strance listu, prohlizec nadava
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # Ted to muze opravit vyplnenim pole nejakym textem
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

        # self.fail('Finish this test!')

    def test_cannot_add_duplicate_items(self):
        # Tania jde na domovskou stranku a zacne novy list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # omylem zkusi zadat stejnou polozku znovu
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # vidi uzitecnou chybovou zpravu
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You've already got this in your list"
        ))

