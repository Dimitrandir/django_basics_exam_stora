from django.core.validators import RegexValidator
from django.db import models

class Employee(models.Model):
    MANAGER = 'Manager'
    CASHIER = 'Cashier'
    WAREHOUSE = 'Warehouse'
    ROLE_CHOOSER = [(MANAGER, 'Manager'), (CASHIER, 'Cashier'),(WAREHOUSE, 'Warehouse')]

    first_name = models.CharField(max_length=30, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=30,blank=False, verbose_name='Last Name')
    phone = models.CharField(max_length=10, blank=True, verbose_name='Phone number')
    email = models.EmailField(unique=True, verbose_name='Email address')
    role = models.CharField(max_length=9, choices=ROLE_CHOOSER, default=CASHIER)
    password = models.CharField(max_length=12, default='1234', validators=[RegexValidator(regex='^\d+$',
                                                                          message='Password must contain only digits.',
                                                                          code='invalid_password')] ,unique=True,
                                help_text='Enter password, digits only')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


