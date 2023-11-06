from django.test import TestCase
from user.models import CustomUser 
from .models import Transaction 

class TransactionModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_create_transaction(self):
        # Create a transaction and associate it with the user
        transaction = Transaction.objects.create(
            amount=100,
            type='expense',
            category='groceries',
            date='2023-11-01',
            user=self.user
        )
        # Perform assertions on the created transaction
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.type, 'expense')
