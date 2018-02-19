from django.db import models

# Create your models here.



class Education (models.Model):
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    degree = models.CharField(max_length=64, null=False, blank=False)
    major = models.CharField(max_length=64, null=False, blank=False)
    gpa = models.FloatField(null=False, blank=False)
