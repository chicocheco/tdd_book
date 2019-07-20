from selenium import webdriver
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
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

# muze rovnou svobodne pridat polozku to-do

# pise "Nakoupit pavi pera" do textoveho pole (rada vyrabi rybi navnady)

# kdyz zmackne enter, stranka se obnovi, a stranka ted zobrazi na seznamu
# "1: Nakoupit pavi pera" jako novou polozku na seznamu to-do

# stale zde je textove pole rikajici si o pridani dalsi polozky
# napise "pouzit pavi pera na vyrobu navnady" (Tania je velmi metodicka)

# stranka se znovu obnovi a ted jsou zobrazeny obe polozky na jejim seznamu

# Tania se zajima, zda si stranka pamatuje jeji seznam. Pak vidi, ze si pro ni
# stranka vygenerovala unikatni URL -- je zde vysvetlujici text k tomuto jevu

# navstivi tuto URL adresu - jeji to-do seznam tam stale je

# uspokojena, jde spat
