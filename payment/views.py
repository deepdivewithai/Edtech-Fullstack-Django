# views.py
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
