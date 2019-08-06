from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    # substitution for implicit wait
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                # WebDriverException for when page hasn't loaded
                # AssertionError for when the table is there but haasn't reloaded yet
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
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

        # a stranka ted zobrazi polozku v ocislovanem seznamu
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # stale zde je textove pole rikajici si o pridani dalsi polozky
        # napise "pouzit pavi pera na vyrobu navnady" (Tania je velmi metodicka)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # seznam se znovu obnovi a ted Tania vidi obe polozky v seznamu
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Tania se zajima, zda si stranka pamatuje jeji seznam. Pak vidi, ze si pro ni
        # stranka vygenerovala unikatni URL -- je zde vysvetlujici text k tomuto jevu

        # navstivi tuto URL adresu - jeji to-do seznam tam stale je
        # uspokojena, jde spat

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Tania si vytvori novy to-do seznam
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # vsimne si, ze jeji seznam ma unikatni URL adresu
        tania_list_url = self.browser.current_url
        self.assertRegex(tania_list_url, '/lists/.+')

        # nyni prijde jeste dalsi uzivatel na stranku, Standa

        ## vytvorime novou kopii prihlizece k ujisteni se, ze zadna z Tanii informaci
        ## neni vyzrazena z cookies atd.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Standa otevre domovskou stranku, kde neni znamky Tanii seznamu
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Standa zacne novy seznam pridavanim novych polozek. Je nudnejsi nez Tanii
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Standa dostane svoji novou unikatni URL
        standa_list_url = self.browser.current_url
        self.assertRegex(standa_list_url, '/lists/.+')
        self.assertNotEqual(standa_list_url, tania_list_url)

        # neni zde znamky Tanii seznamu ani ted
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # uspokojeni, jdou oba do postele

        self.fail('Finish the test!')
