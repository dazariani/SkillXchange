from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
  isTutor = models.BooleanField(default=False)
  isStudent = models.BooleanField(default=False)


class SkillClass(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  startDateTime = models.TimeField(default='14:30')
  maxStudents = models.IntegerField()
  tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Enrollment(models.Model):
  student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  skillClass = models.ForeignKey(SkillClass, on_delete=models.CASCADE)


class Review(models.Model):
  skillClass = models.ForeignKey(SkillClass, on_delete=models.CASCADE)
  client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  text = models.TextField(max_length=300)
  stars = models.IntegerField()

