# models.py
from django.db import models
from user.models import Student

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student.name
