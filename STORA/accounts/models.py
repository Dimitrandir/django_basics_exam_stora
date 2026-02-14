from django.db import models

class Employee(models.Model):
# Roles
    MANAGER = 'Manager'
    CASHIER = 'Cashier'
    WAREHOUSE = 'Warehouse'
    ROLE_CHOOSER = [(MANAGER, 'Manager'), (CASHIER, 'Cashier'),(WAREHOUSE, 'Warehouse')]

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30,blank=False)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=9, choices=ROLE_CHOOSER, default=CASHIER)
    password = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


