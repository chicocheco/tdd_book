from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # tania slysela o husty novy apce to-do
        # jde se na to mrknout
        self.browser.get('http://localhost:8000')

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
        inputbox.send_keys('Buy peacock feathers.')

        # kdyz zmackne enter, stranka se obnovi, a stranka ted zobrazi na seznamu
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # stale zde je textove pole rikajici si o pridani dalsi polozky
        # napise "pouzit pavi pera na vyrobu navnady" (Tania je velmi metodicka)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()





# stranka se znovu obnovi a ted jsou zobrazeny obe polozky na jejim seznamu

# Tania se zajima, zda si stranka pamatuje jeji seznam. Pak vidi, ze si pro ni
# stranka vygenerovala unikatni URL -- je zde vysvetlujici text k tomuto jevu

# navstivi tuto URL adresu - jeji to-do seznam tam stale je

# uspokojena, jde spat
