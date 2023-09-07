from django.urls import path
from .views import AnalyticsDataCreate, AnalyticsDataList

app_name = 'Analytics'

urlpatterns = [
    path('analytics/', AnalyticsDataList.as_view(), name='analytics_list'),
    path('users/<int:pk>/analytics/', AnalyticsDataCreate.as_view(), name='analytics-create'),
]
