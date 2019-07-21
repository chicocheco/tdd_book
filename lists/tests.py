from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        # .func = view function that would be used to serve the URL
        # we get Resolver404 - "/" is not mapped to home_page view yet
        self.assertEqual(found.func, home_page)
