from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

# Create your tests here.


class TestUrls(TestCase):
    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func.view_class, HomePageView)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func.view_class, AboutPageView)
