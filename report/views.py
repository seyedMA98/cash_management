from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from transactions.models import Transaction
from django.db.models import Q

class MonthlySummaryReport(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Get query parameters for month and year
        month = request.data.get('month')
        year = request.data.get('year')

        if not month or not year:
            return Response({"error": "Both 'month' and 'year' parameters are required."}, status=400)

        # Replace with your logic to retrieve the user's monthly summary
        user = request.user

        # Calculate monthly income and expenses
        monthly_summary = Transaction.objects.filter(user=user, date__month=month, date__year=year).aggregate(
            total_income=Sum('amount', filter=(Q(type='income') & Q(date__month=month) & Q(date__year=year))),
            total_expenses=Sum('amount', filter=(Q(type='expense') & Q(date__month=month) & Q(date__year=year)))
        )

        return Response({
            "month": month,
            "year": year,
            "total_income": monthly_summary['total_income'] or 0,
            "total_expenses": monthly_summary['total_expenses'] or 0,
        })