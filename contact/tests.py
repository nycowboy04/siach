from django.test import TestCase

from . import views
# Create your tests here.
class ContactPageTests(TestCase):

    def test_contact_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)

    def test_url_by_name(self):
        response=self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'email.html')

    def test_contact_page_contains_correct_html(self):
        response=self.client.get('/')
        self.assertContains(response,'<h1>Contact Us</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response=self.client.get('/')
        self.assertNotContains( response,'Hi there! I should not be on this page.')
