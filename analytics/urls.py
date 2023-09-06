from django.urls import path
from .views import AnalyticsDataCreateView

app_name = 'Analytics'

urlpatterns = [
    path('analytics/', AnalyticsDataCreateView.as_view(), name='analytics-create'),
]
