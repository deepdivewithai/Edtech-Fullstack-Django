from django.urls import path
from .views import TeacherViewSet, StudentViewSet

app_name = 'user_list'

urlpatterns = [
    path('teachers/', TeacherViewSet.as_view(), name='teacher_list'),
    path('students/', StudentViewSet.as_view(), name='student_list')
]