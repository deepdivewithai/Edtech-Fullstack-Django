from django.urls import path
from . import views

app_name = 'payment_done'

urlpatterns = [
    path('payments/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('students/<int:pk>/payments/', views.PaymentListView.as_view(), name='payment-list'),
]