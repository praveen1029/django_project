from django.db import models

# Create your models here.

class dummy_model(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)