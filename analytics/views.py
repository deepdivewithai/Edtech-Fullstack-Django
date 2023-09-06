from rest_framework import generics
from .models import AnalyticsData
from .serializers import AnalyticsDataSerializer

class AnalyticsDataCreateView(generics.CreateAPIView):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer


# Collect and store analytics data in your views or other application logic
def track_analytics_event(request):
    event_name = "User Login"  # Replace with the actual event name
    user = request.user  # Assuming you have user authentication in place

    # Additional data specific to the event
    # ...

    # Create and save the analytics data
    analytics_data = AnalyticsData(event_name=event_name, user=user)
    analytics_data.save()
