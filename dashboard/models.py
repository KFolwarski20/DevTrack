from django.db import models
from django.contrib.auth.models import User


class ProgrammingLog(models.Model):
    LANGUAGE_CHOICES = [
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('c#', 'C#'),
        ('html', 'HTML'),
        ('sql', 'SQL'),
        ('go', 'Go'),
        ('ruby', 'Ruby'),
        ('c++', 'C++'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.language} - {self.hours}h"

    @classmethod
    def ensure_user_logs(cls, user):
        """ Create missing logs for the new User """
        existing_logs = ProgrammingLog.objects.filter(user=user).values_list('language', flat=True)
        missing_logs = [lang for lang, _ in cls.LANGUAGE_CHOICES if lang not in existing_logs]

        for lang in missing_logs:
            cls.objects.create(user=user, language=lang, hours=0)
