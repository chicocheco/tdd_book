from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Tania jde na domovskou stranku
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # vsimne si, ze vstupni pole je vycentrovano
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # ona zacne novy seznam a vidi ze vstupni pole pro seznam je take vycentrovane
        self.add_list_item('testing')
        # lists/1/...
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
