from rest_framework import serializers
from .models import AnalyticsData

class AnalyticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsData
        fields = '__all__'
