from django.urls import path

from STORA.reports.views import (
    ReportsDashboardView,
    SalesReportView,
    DeliveriesReportView,
)

urlpatterns = [
    path('', ReportsDashboardView.as_view(), name='reports_dashboard'),
    path('sales/', SalesReportView.as_view(), name='sales_report'),
    path('deliveries/', DeliveriesReportView.as_view(), name='deliveries_report'),
]