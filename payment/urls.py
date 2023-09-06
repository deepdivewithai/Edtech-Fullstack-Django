# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_subscription/', views.create_subscription, name='create_subscription'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_history/', views.payment_history, name='payment_history'),
    # Define other URL patterns for your application
]
