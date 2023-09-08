from .models import TeacherDetails, StudentDetails
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetails
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'