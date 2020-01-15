from django.conf import settings
from django.contrib.auth import get_user_model
from .management.commands.create_session import create_pre_authenticated_session
from .server_tools import create_session_on_server
from .base import FunctionalTest

User = get_user_model()


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)

        ## to set a cookie we need to first visit the domain
        ## 404 pages load the fastest!
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,  # default is 'sessionid'
            value=session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Tania je prihlasena uzivatelka
        self.create_pre_authenticated_session('tania@example.com')

        # jde na domovskou stranku a zacit novy seznam
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')  # TODO: define new helper in base.py
        self.add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # vsimne si poprve odkazu "My lists"
        self.browser.find_element_by_link_text('My lists').click()

        # vidi, ze zde je jeji seznam, pojmenovan dle prvni polozky seznamu
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
        )
        self.browser.find_element_by_link_text('Reticulate splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # rozhodne se zacit dalsi seznam, jen tak pro kontrolu
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # jeji novy seznam se objevi pod "My lists"
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # odhlasi se a odkaz "My lists" zmizi
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))
