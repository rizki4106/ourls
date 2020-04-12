from django.db import models

# Create your models here.

class Parse(models.Model):

    url = models.TextField()
    parse = models.CharField(max_length=5)
    tanggal = models.DateField()