from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # tania slysela o husty novy apce to-do
        # jde se na to mrknout
        self.browser.get(self.live_server_url)

        # vsimne si, ze titulek stranky a zahlavi zminuji to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # muze rovnou svobodne pridat polozku to-do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # pise "Nakoupit pavi pera" do textoveho pole (rada vyrabi rybi navnady)
        inputbox.send_keys('Buy peacock feathers')
        # kdyz zmackne enter, stranka se obnovi
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # a stranka ted zobrazi polozku v ocislovanem seznamu
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # stale zde je textove pole rikajici si o pridani dalsi polozky
        # napise "pouzit pavi pera na vyrobu navnady" (Tania je velmi metodicka)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # seznam se znovu obnovi a ted Tania vidi obe polozky v seznamu
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Tania se zajima, zda si stranka pamatuje jeji seznam. Pak vidi, ze si pro ni
        # stranka vygenerovala unikatni URL -- je zde vysvetlujici text k tomuto jevu

        # navstivi tuto URL adresu - jeji to-do seznam tam stale je
        # uspokojena, jde spat

        self.fail('Finish the test!')
