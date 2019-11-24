from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    # YAGNI, 3 strikes and refactor, not moving helper methods to base.py if not needed elsewhere
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Tania jde na domovskou stranku a omylem zkusi na seznam pridat prazdny text.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)  # every click or enter should be followed by some wait

        # prohlizec zastavi pozadavek protoze jsme nezadali nic do 'required' policka
        # (HTML5) browser adds a CSS pseudoselector ":invalid" to the id parameter of the element
        # and pops up "Fill out the field" alert
        # fallback: if the browser like Safari, does not fully implement HTML5, so the custom error message will be used
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        """
        lambda: when you want to save a function with arguments to a variable/parameter but not executing it yet
        >>> myfn = lambda: addthree(2) # note addthree is not called immediately here
        >>> myfn
        <function <lambda> at 0x7f3b140339d8>
        >>> myfn() # execute it here
        5
        """

        # Nyni to zkusi znovu s nejakym textem pro polozku, coz funguje, chyba zmizi
        # CSS pseudoselector changes from #id_text:invalid to #id_text:valid
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))

        # a muze bez problemu potvrdit predmet
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Skodolibe, ted zkusi znovu pridat druhou prazdnou polozku (jiz pro existujici seznam)
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

        # omylem zkusi zadat stejnou polozku znovu (novy list jiz existuje)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # vidi uzitecnou chybovou zpravu ze zadava duplikat
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        # Tania otevre novy seznam a zpusobi validaci error
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Banter too thick')
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # zacne neco psat do policka aby zmizela chybova hlaska o jiz existujici polozce
        self.get_item_input_box().send_keys('a')

        # ma radost, ze chybova hlaska zmizi
        self.wait_for((lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        )))