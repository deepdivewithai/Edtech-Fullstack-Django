from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer


class TeacherViewSet(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

