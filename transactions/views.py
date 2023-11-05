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

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        # Get user data from the request
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            # Log the user in
            login(request, user)

            # Get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        # Get user data from the request
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, password=password)

        # Authenticate the user to generate a token (you can use TokenAuthentication)
        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "User registration successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "User registration failed"}, status=status.HTTP_400_BAD_REQUEST)

class TransactionList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
            return Transaction.objects.filter(user=self.request.user)
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Associate the transaction with the authenticated user
        serializer.save(user=self.request.user)

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
            return Transaction.objects.filter(user=self.request.user)
    serializer_class = TransactionSerializer
