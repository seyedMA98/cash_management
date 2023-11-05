from django.urls import path
from .views import *

urlpatterns = [
    path('list/', TransactionList.as_view(), name='transaction-list'),
    path('list/<str:category>/', TransactionList.as_view(), name='transaction-list'),
    path('list/<str:category>/<str:type>/', TransactionList.as_view(), name='transaction-list'),
    path('list/<str:category>/<str:type>/<str:sort_by>/', TransactionList.as_view(), name='transaction-list'),
    path('detail/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('balance/', BalanceView.as_view(), name='balance'),
]