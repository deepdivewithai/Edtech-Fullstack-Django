# views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription, Payment

# @login_required
# def create_subscription(request):
#     if request.method == 'POST':
#         # Get the selected subscription plan from the form
#         selected_plan = request.POST.get('selected_plan')  # Assuming you have a form field for selecting a plan

#         # Calculate subscription start and end dates based on the selected plan
#         # Implement your logic here to determine the start and end dates

#         # Create a new Subscription instance for the user
#         subscription = Subscription(user=request.user, plan=selected_plan, start_date=start_date, end_date=end_date)
#         subscription.save()

#         # Redirect to a success page or perform other actions
#         return redirect('subscription_success')
#     else:
#         # Render a page where users can choose a subscription plan
#         return render(request, 'payment/choose_plan.html')



# @login_required
# def process_payment(request):
#     if request.method == 'POST':
#         # Get the payment amount from the form
#         payment_amount = request.POST.get('payment_amount')  # Assuming you have a form field for entering payment amount

#         # Create a new Payment instance for the user
#         payment = Payment(user=request.user, amount=payment_amount)
#         payment.save()

#         # Update the user's subscription status based on the payment
#         # Implement your logic here to update the subscription status

#         # Redirect to a success page or perform other actions
#         return redirect('payment_success')
#     else:
#         # Render a page where users can make a payment
#         return render(request, 'payment/make_payment.html')



# @login_required
# def payment_history(request):
#     # Retrieve the user's payment history
#     payments = Payment.objects.filter(user=request.user)

#     # Render a template to display payment history
#     return render(request, 'payment/history.html', {'payments': payments})


