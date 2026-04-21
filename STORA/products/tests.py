from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from STORA.products.models import Product, Barcode


User = get_user_model()


class ProductApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='pass12345',
        )
        self.client.login(username='testuser', password='pass12345')

        self.product = Product.objects.create(
            internal_code='P0000001',
            name='Test Product',
            delivery_price=2.50,
            sell_price=3.50,
            quantity=10,
        )
        Barcode.objects.create(
            code='1234567890123',
            product=self.product,
        )

    def test_products_api_returns_200_for_authenticated_user(self):
        response = self.client.get(reverse('api_products'))
        self.assertEqual(response.status_code, 200)

    def test_products_api_returns_product_data(self):
        response = self.client.get(reverse('api_products'))
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Test Product')

    def test_products_api_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('api_products'))
        self.assertIn(response.status_code, (302, 401, 403))
