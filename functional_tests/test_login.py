import os
import poplib
import time
import re

from django.core import mail
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def wait_for_email(self, test_email, subject):
        if not self.staging_server:
            email = mail.outbox[0]
            self.assertIn(test_email, email.to)
            self.assertEqual(subject, email.subject)
            return email.body

        email_id = None
        start = time.time()
        inbox = poplib.POP3_SSL('pop.mail.yahoo.com')
        try:
            inbox.user(test_email)
            inbox.pass_(os.environ['YAHOO_PASSWORD'])
            while time.time() - start < 60:
                # get 10 newest messages
                count, _ = inbox.stat()
                for i in reversed(range(max(1, count - 10), count + 1)):
                    print('getting msg', i)
                    _, lines, __ = inbox.retr(i)
                    lines = [line.decode('utf8') for line in lines]
                    print(lines)
                    if f'Subject: {subject}' in lines:
                        email_id = i
                        body = '\n'.join(lines)
                        return body
        finally:
            if email_id:
                inbox.dele(email_id)
            inbox.quit()

    def test_can_get_email_link_to_log_in(self):
        # Tania jde stranku a poprve si vsimne sekce "Log in" v navbaru
        # rika ji to aby zadala svoji emailovou adresu a udela tak
        if self.staging_server:
            test_email = 'testuser.2020@yahoo.com'
        else:
            test_email = 'tania@example.com'
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(test_email)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # objevi se zprava ze byl odeslan email
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # zkontroluje svoje emaily a najde zpravu
        ## Django gives us access to any emails the server tries to send via the mail.outbox attribute - mocked out
        body = self.wait_for_email(test_email, SUBJECT)

        # ma v sobe URL odkaz
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # klikne na nej
        self.browser.get(url)

        # prihlasi se!
        self.wait_to_be_logged_in(email=test_email)

        # ted se odhlasi
        self.browser.find_element_by_link_text('Log out').click()

        # je odhlasena
        self.wait_to_be_logged_out(email=test_email)
        # TODO: does 'source .env' do the same as gunicorn .service?