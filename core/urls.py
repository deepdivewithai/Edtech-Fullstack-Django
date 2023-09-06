from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls', namespace='user_list')),
    path('', include('content.urls', namespace='content_list')),
    path('', include('chat.urls', namespace='load_chat')),
    path('', include('analytics.urls', namespace='Analytics'))
]
