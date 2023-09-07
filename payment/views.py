# views.py
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer