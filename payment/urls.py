# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.PaymentList.as_view(), name='payment-list'),
    # Define additional URL patterns for payment-related operations
]