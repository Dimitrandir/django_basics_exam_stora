from django.apps import apps
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name not in {'STORA.accounts', 'STORA.products', 'STORA.sales'}:
        return

    managers_group, _ = Group.objects.get_or_create(name='Managers')
    cashiers_group, _ = Group.objects.get_or_create(name='Cashiers')
    warehouse_group, _ = Group.objects.get_or_create(name='Warehouse')

    managers_group.permissions.set(Permission.objects.all())

    sale_permissions = Permission.objects.filter(
        content_type__app_label='sales'
    )
    cashiers_group.permissions.set(sale_permissions)

    product_permissions = Permission.objects.filter(
        content_type__app_label='products',
        codename__in=[
            'view_product',
            'add_product',
            'change_product',
            'view_category',
            'add_category',
            'change_category',
            'view_suppliers',
            'add_suppliers',
            'change_suppliers',
        ]
    )
    warehouse_group.permissions.set(product_permissions)