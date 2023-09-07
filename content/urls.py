from django.urls import path
from .views import ContentListView, ContentDetailView

app_name = 'content_list'

urlpatterns = [
    path('teachers/<int:pk>/students/content/', ContentListView.as_view(), name='content-list-create'),
    path('teachers/content/', ContentDetailView.as_view(), name='content-detail'),
]
