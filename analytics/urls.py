from django.urls import path
from .views import AnalyticsDataList

app_name = 'Analytics'

urlpatterns = [
    path('users/<int:pk>/analytics/', AnalyticsDataList.as_view(), name='analytics-create'),
]
