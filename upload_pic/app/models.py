from django.db import models


# Create your models here.

class MyObject(models.Model):
    name = models.CharField(max_length=512)
    source = models.FileField()
    alt_name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
