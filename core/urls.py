from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls', namespace='user_list')),
    path('', include('content.urls', namespace='content_list')),
    path('', include('analytics.urls', namespace='Analytics')),
    path('', include('payment.urls', namespace='payment_done'))
]
