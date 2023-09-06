from rest_framework import generics
from .models import AnalyticsData
from .serializers import AnalyticsDataSerializer

class AnalyticsDataList(generics.ListAPIView):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer
    