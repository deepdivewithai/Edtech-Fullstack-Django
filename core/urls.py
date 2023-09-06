from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls', namespace='user_list')),
    path('', include('content.urls', namespace='content_list')),
    path('', include('analytics.urls', namespace='Analytics')),
    path('', include('payment.urls', namespace='payment_done'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)