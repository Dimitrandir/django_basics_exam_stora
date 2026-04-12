from django.urls import path
from . import views
from .views import DeliveryListView, DeliveryDeleteView, DeliveryDetailView, deliveries_add

urlpatterns = [ path('', DeliveryListView.as_view(), name='deliveries_list'),
                path('add/', views.deliveries_add, name='delivery_add'),
                path('<int:pk>/', DeliveryDetailView.as_view(), name='delivery_details'),
                path('delete/<int:pk>/', DeliveryDeleteView.as_view(), name='delivery_delete'),
                ]