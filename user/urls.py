from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'user_list'

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]