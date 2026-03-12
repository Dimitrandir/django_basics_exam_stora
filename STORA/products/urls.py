from django.urls import path
from . import views

urlpatterns = [path('', views.products_list, name= 'product_list'),
               path('create/', views.product_create, name='product_create'),
               path('<int:pk>/', views.product_details, name='product_details'),
               path('edit/<int:pk>/', views.product_edit, name='product_edit'),
               path('delete/<int:pk>/', views.product_delete, name='product_delete'),
               path('barcodes/', views.barcode_list, name='barcode_list'),
               ]