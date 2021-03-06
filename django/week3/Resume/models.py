from django.db import models
from datetime import date

# Create your models here.



class Education (models.Model):
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    degree = models.CharField(max_length=64, null=False, blank=False)
    major = models.CharField(max_length=64, null=False, blank=False)
    gpa = models.FloatField(null=False, blank=True)

class Experience (models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    description = models.TextField(max_length=64, null=False, blank=True)
