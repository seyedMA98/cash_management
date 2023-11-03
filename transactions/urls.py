from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('list/', TransactionList.as_view(), name='transaction-list'),
    path('detail/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('create-transaction/', create_transaction, name='create-transaction'),
]