from django.db import models

# Create your models here.

class Link(models.Model):
    shortened = models.CharField(max_length=300)
    original = models.CharField(max_length=1000)

    def __str__(self):
        return self.shortened