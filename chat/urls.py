from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'load_chat'

router = DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Other URL patterns for chat rooms, user interactions, etc.
]