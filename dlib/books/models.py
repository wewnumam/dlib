from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    writer = models.CharField(max_length=64)
    synopsis = models.TextField()

    def __str__(self):
        return "{}".format(self.title)
    
    