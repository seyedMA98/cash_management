from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TransactionSerializer
from .models import Transaction
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TransactionList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)  # Filter transactions for the authenticated user

        # Filtering options
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        type = self.request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)

        # Sorting options
        sort_by = self.request.query_params.get('sort_by')
        if sort_by == 'date':
            queryset = queryset.order_by('date')  # Sort by date
        elif sort_by == 'amount':
            queryset = queryset.order_by('amount')  # Sort by amount
        
        return queryset

    def perform_create(self, serializer):
        # Associate the transaction with the authenticated user
        serializer.save(user=self.request.user)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
            return Transaction.objects.filter(user=self.request.user)
    serializer_class = TransactionSerializer

class BalanceView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user  # The authenticated user
        balance = user.balance  # Replace with your logic to retrieve the user's balance

        return Response({"balance": balance}, status=status.HTTP_200_OK)