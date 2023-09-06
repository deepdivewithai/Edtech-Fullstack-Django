from django.urls import path
from . import views

app_name = 'payment_done'

urlpatterns = [
    path('users/<int:pk>/payments/', views.PaymentList.as_view(), name='payment-list'),
]