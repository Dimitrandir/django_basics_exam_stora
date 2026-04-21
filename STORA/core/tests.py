from django.test import TestCase
from django.urls import reverse


class IndexPageTests(TestCase):
    def test_index_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')