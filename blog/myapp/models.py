from django.db import models

class MyModel2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
