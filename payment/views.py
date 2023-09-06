# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Subscription, Payment

# @login_required
# def create_subscription(request):
    # Implement subscription creation logic
    # This view should create a new Subscription instance for the user


# @login_required
# def process_payment(request):
#     pass
    # Implement payment processing logic
    # This view should create a new Payment instance for the user


@login_required
def payment_history(request):
    # Retrieve and display the user's payment history
    payments = Payment.objects.filter(user=request.user)
    # Render a template to display payment history
    return render(request, 'payment/history.html', {'payments': payments})

