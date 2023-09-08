from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import TeacherDetails, StudentDetails, Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer


class TeacherViewSet(ListCreateAPIView):
    queryset = TeacherDetails.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(ListCreateAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentSerializer



