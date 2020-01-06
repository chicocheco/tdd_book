from django.core import mail
from selenium.webdriver.common.keys import Keys
import re

from .base import FunctionalTest

TEST_MAIL = 'edith@example.com'
SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # Tania jde stranku a poprve si vsimne sekce "Log in" v navbaru
        # rika ji to aby zadala svoji emailovou adresu a udela tak
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_MAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # objevi se zprava ze byl odeslan email
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # zkontroluje svoje emaily a najde zpravu
        ## Django gives us access to any emails the server tries to send via the mail.outbox attribute - mocked out
        email = mail.outbox[0]
        self.assertIn(TEST_MAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)

        # ma v sobe URL odkaz
        self.assertIn('Use this link to log in', email.body)
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # klikne na nej
        self.browser.get(url)

        # prihlasi se!
        self.wait_to_be_logged_in(email=TEST_MAIL)

        # ted se odhlasi
        self.browser.find_element_by_link_text('Log out').click()

        # je odhlasena
        self.wait_to_be_logged_out(email=TEST_MAIL)
