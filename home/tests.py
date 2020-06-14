from django.test import SimpleTestCase # to be used when there is no model involvement
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.

class HomePageTest (SimpleTestCase):


    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_homepage_status(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_url(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_url_resolves_homepageview(self): # url is linked with correct view name
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, HomePageView.as_view().__name__
        )

class AboutUsPageTest (SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
