from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        # .func = view function that would be used to serve the URL
        # we get Resolver404 - "/" is not mapped to home_page view yet
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # what Django sees when a user's browser asks for a page is HttpRequest()
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
