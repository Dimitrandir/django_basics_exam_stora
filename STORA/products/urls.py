from django.urls import path
from .views import (ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, ProductDetailView,
                    BarcodeListView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView,
                    SuppliersListView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView)

urlpatterns = [path('', ProductListView.as_view(), name= 'product_list'),
               path('create/', ProductCreateView.as_view(), name='product_create'),
               path('<int:pk>/', ProductDetailView.as_view(), name='product_details'),
               path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
               path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
               path('barcodes/', BarcodeListView.as_view(), name='barcode_list'),
               path('categories/', CategoryListView.as_view(), name='category_list'),
               path('categories/add/', CategoryCreateView.as_view(), name='category_create'),
               path('categories/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
               path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
               path('suppliers/', SuppliersListView.as_view(), name='suppliers_list'),
               path('suppliers/add/', SupplierCreateView.as_view(), name='suppliers_create'),
               path('suppliers/edit/<int:pk>/', SupplierUpdateView.as_view(), name='suppliers_edit'),
               path('suppliers/delete/<int:pk>/', SupplierDeleteView.as_view(), name='suppliers_delete'),

               ]