from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from STORA.products.models import Product
from STORA.sales.models import SaleAttributes, SaleItems
from STORA.sales.forms import SaleItemForm


User = get_user_model()


class SalesViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='cashier',
            password='pass12345',
        )
        self.client.login(username='cashier', password='pass12345')

        self.product = Product.objects.create(
            internal_code='P0000003',
            name='Sale Product',
            delivery_price=2.00,
            sell_price=3.00,
            quantity=10,
        )

    def test_sales_add_page_loads(self):
        response = self.client.get(reverse('sale_add'))
        self.assertEqual(response.status_code, 200)

    def test_sales_list_page_loads(self):
        response = self.client.get(reverse('sales_list'))
        self.assertEqual(response.status_code, 200)

    def test_sale_details_page_loads(self):
        sale = SaleAttributes.objects.create(cashier=self.user)
        response = self.client.get(reverse('sale_details', kwargs={'pk': sale.pk}))
        self.assertEqual(response.status_code, 200)

    def test_sale_delete_page_loads(self):
        sale = SaleAttributes.objects.create(cashier=self.user)
        response = self.client.get(reverse('sale_delete', kwargs={'pk': sale.pk}))
        self.assertEqual(response.status_code, 200)

    def test_sale_item_model_can_be_created(self):
        sale = SaleAttributes.objects.create(cashier=self.user)
        item = SaleItems.objects.create(
            sale=sale,
            sale_item=self.product,
            sale_quantity=2,
            price_at_sale=3.00,
            total_price_row=6.00,
        )
        self.assertEqual(item.total_price_row, 6.00)

    def test_sale_add_page_uses_template(self):
        response = self.client.get(reverse('sale_add'))
        self.assertTemplateUsed(response, 'sales/sale_add.html')


class SaleFormValidationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            internal_code='P0000004',
            name='Validation Product',
            delivery_price=2.00,
            sell_price=3.00,
            quantity=10,
        )

    def test_sale_item_form_requires_quantity(self):
        form_data = {
            'sale_item': self.product.pk,
            'sale_quantity': '',
            'price_at_sale': '3.00',
            'total_price_row': '6.00',
        }
        form = SaleItemForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_sale_item_form_requires_item(self):
        form_data = {
            'sale_item': '',
            'sale_quantity': '2',
            'price_at_sale': '3.00',
            'total_price_row': '6.00',
        }
        form = SaleItemForm(data=form_data)
        self.assertFalse(form.is_valid())
