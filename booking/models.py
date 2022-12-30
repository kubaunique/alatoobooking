from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Football field", "Football field"),
    ("Basketball field", "Basketball field"),
    ("Volleyball field", "Volleyball field"),
    ("Gym", "Gym"),
    )
TIME_CHOICES = (
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Football field")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="4 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"