from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    MANAGER = 'Manager'
    CASHIER = 'Cashier'
    WAREHOUSE = 'Warehouse'
    ROLE_CHOOSER = [(MANAGER, 'Manager'), (CASHIER, 'Cashier'),(WAREHOUSE, 'Warehouse')]

    phone = models.CharField(max_length=10, blank=True, verbose_name='Phone number')
    role = models.CharField(max_length=9, choices=ROLE_CHOOSER, default=CASHIER)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


