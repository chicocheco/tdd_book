from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import WebDriverException
import time
import os
from .server_tools import reset_database

MAX_WAIT = 10


# wait decorator
def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)  # decorated
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return modified_fn  # not calling it with ()!


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)
        # always set the env.variable inline, do not "export"
        # STAGING_SERVER=chicocheco.xyz python manage.py test functional_tests
        self.staging_server = os.environ.get('STAGING_SERVER')
        if self.staging_server:
            self.live_server_url = 'http://' + self.staging_server  # saving the variable on self to use elsewhere too
            reset_database(self.staging_server)

    def tearDown(self):
        self.browser.quit()

    # substitution for implicit wait
    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
                # return its return value to be able to exit the loop immediately if no exception is raised
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)
