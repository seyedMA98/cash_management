from django.urls import path
from .views import *

urlpatterns = [
    path('monthly-summary/', MonthlySummaryReport.as_view(), name='monthly-summary-report'),
]