import os
import poplib
import time
import re
from contextlib import contextmanager

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

        @contextmanager  # in order to see a change in the message count each time through the loop
        def pop_inbox():
            try:
                inbox_yahoo = poplib.POP3_SSL('pop.mail.yahoo.com')
                inbox_yahoo.user(test_email)
                inbox_yahoo.pass_(os.environ.get('YAHOO_PASSWORD'))  # must be exported first
                yield inbox_yahoo
            finally:
                # the mailbox on the server is locked until quit() is called
                inbox_yahoo.quit()

        start = time.time()
        while time.time() - start < 60:
            with pop_inbox() as inbox:
                time.sleep(.5)
                count, _ = inbox.stat()  # (message count, mailbox size)
                last_index = max(0, count - 5)
                print(f'Found {count} emails in inbox of {test_email}. Checking from {count} to {last_index + 1}.')
                time.sleep(.5)
                for i in range(count, last_index, -1):  # the higher index, the newer email
                    _, lines, __ = inbox.retr(i)  # (response, ['line', ...], octets)
                    lines = [line.decode('utf8') for line in lines]
                    if f'Subject: {subject}' in lines:
                        time.sleep(.5)
                        inbox.dele(i)
                        body = '\n'.join(lines)
                        # print(body)
                        return body  # finish wait_for_email() here
            print('re-trying to find the email in 5 secs...')
            time.sleep(5)

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
        time.sleep(.5)  # give it time to receive the email
        body = self.wait_for_email(test_email, SUBJECT)

        # ma v sobe URL odkaz
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{body}')
        url = url_search.group(0)
        print('login url: ', url)
        self.assertIn(self.live_server_url, url)

        # klikne na nej
        self.browser.get(url)

        # prihlasi se!
        self.wait_to_be_logged_in(email=test_email)

        # ted se odhlasi
        time.sleep(2)
        self.browser.find_element_by_link_text('Log out').click()  # proof we are logged in, if found

        # je odhlasena
        self.wait_to_be_logged_out(email=test_email)
        # TODO: does 'source .env' do the same as gunicorn .service?
