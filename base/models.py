from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.TextField(max_length=200)
    school = models.TextField(max_length=200)
    university = models.TextField(max_length=200)
    previous_work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=1000)

