from django.urls import path
from . import views

urlpatterns = [ path('', views.sales_list, name='sales_list'),
                path('add/', views.sales_add, name='sale_add'),
                path('<int:pk>/', views.sale_details, name='sale_details'),
                path('edit/<int:pk>/', views.sale_edit, name='sale_edit'),
                path('delete/<int:pk>/', views.sale_delete, name='sale_delete'),
                ]