from django.db import models
from django.contrib.auth.models import User


class ProgrammingLog(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('c++', 'C++'),
        ('go', 'Go'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.language} - {self.hours}h"