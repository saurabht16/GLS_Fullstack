from .views import index
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_index_view(self):
        """
        Test to check if the correct view is being called when running the page
        """
        found = resolve('/')
        self.assertEqual(found.func, index)


    def test_home_page_returns_correct_html(self):
        """
        Test to check if the correct html page is being returned
        """
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>GLS Fullstack Exercise</title>', html)
        self.assertIn('<script src="/static/js/player.js"></script>', html)
        self.assertTrue(html.endswith('</html>'))

