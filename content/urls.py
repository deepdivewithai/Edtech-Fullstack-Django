from django.urls import path
from .views import ContentListCreateView, ContentDetailView

app_name = 'content_list'

urlpatterns = [
    path('content/', ContentListCreateView.as_view(), name='content-list-create'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name='content-detail'),
    # Other URL patterns for content-related views and actions.
]
