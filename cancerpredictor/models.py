from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentby')
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user.username} -> {self.message}"

class PatientData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    res = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} has {self.res}"