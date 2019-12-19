from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self):
        # Tania slysela o husty novy apce to-do a jde se na to mrknout
        self.browser.get(self.live_server_url)

        # vsimne si, ze titulek stranky a zahlavi zminuji "To-do"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # muze pridat novou polozku, protoze ji to napovida text v prazdnem poli
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # pise do tohoto pole "Nakoupit pavi pera" do textoveho pole (rada vyrabi rybi navnady)
        inputbox.send_keys('Buy peacock feathers')
        # kdyz stiskne enter, stranka se obnovi
        inputbox.send_keys(Keys.ENTER)

        # a stranka ted zobrazi polozku v ocislovanem seznamu, zacinajici cislem 1
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # stale zde je textove pole rikajici si o pridani polozky
        # napise "pouzit pavi pera na vyrobu navnady" (Tania je velmi metodicka)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # seznam se znovu obnovi (chvili to trva) a ted Tania vidi obe polozky v seznamu
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Tania si vytvori novy to-do seznam a ukazuje to Standovi
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Tania si vsimne, ze jeji seznam ma unikatni URL adresu
        tania_list_url = self.browser.current_url
        self.assertRegex(tania_list_url, '/lists/.+')  # example: lists/1

        # nyni si to zkusi Standa

        ## vytvorime novou kopii prohlizece (zamezime tomu, ze by se neco nahralo z cookies atd.)
        self.browser.quit()
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)

        # Standa otevre domovskou stranku, kde neni znamky Tanii seznamu
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Standa vytvori novy seznam pridavanim novych polozek. Je nudnejsi nez Tanii
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Standa dostane svoji novou unikatni URL
        standa_list_url = self.browser.current_url
        self.assertRegex(standa_list_url, '/lists/.+')  # example: lists/2
        self.assertNotEqual(standa_list_url, tania_list_url)

        # neni zde znamky Tanii seznamu ani ted (na strance s polozkami)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # uspokojeni, jdou oba do postele
