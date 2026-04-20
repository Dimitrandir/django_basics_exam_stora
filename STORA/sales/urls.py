from django.urls import path
from . import views
from .views import SalesListView, SalesDeleteView, SalesDetailView

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
    path('add/', views.sales_add, name='sale_add'),
    path('draft/save/', views.sales_draft_save, name='sale_draft_save'),
    path('<int:pk>/', SalesDetailView.as_view(), name='sale_details'),
    path('delete/<int:pk>/', SalesDeleteView.as_view(), name='sale_delete'),
]