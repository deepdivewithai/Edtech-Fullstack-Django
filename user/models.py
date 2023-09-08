from django.db import models

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()

    def __str__(self):
        return self.username
    
class TeacherDetails(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    qualification = models.CharField()

    def __str__(self) -> str:
        return self.teacher.username

class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()

    def __str__(self):
        return self.username
    
class StudentDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade_level = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='students_taught')

    def __str__(self) -> str:
        return self.student.username

