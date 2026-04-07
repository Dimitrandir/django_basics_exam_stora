from django.urls import path
from . import views

urlpatterns = [path('', views.products_list, name= 'product_list'),
               path('create/', views.product_create, name='product_create'),
               path('<int:pk>/', views.product_details, name='product_details'),
               path('edit/<int:pk>/', views.product_edit, name='product_edit'),
               path('delete/<int:pk>/', views.product_delete, name='product_delete'),
               path('barcodes/', views.barcode_list, name='barcode_list'),
               path('categories/', views.category_list, name='category_list'),
               path('categories/add/', views.category_create, name='category_create'),
               path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
               path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
               path('suppliers/', views.suppliers_list, name='suppliers_list'),
               path('suppliers/add/', views.suppliers_create, name='suppliers_create'),
               path('suppliers/edit/<int:pk>/', views.suppliers_edit, name='suppliers_edit'),
               path('suppliers/delete/<int:pk>/', views.suppliers_delete, name='suppliers_delete'),

               ]