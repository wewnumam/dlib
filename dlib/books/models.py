from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    writer = models.CharField(max_length=64)
    synopsis = models.TextField()
    cover = models.FileField(upload_to='static/uploads/', max_length=128, default='default.jpg')
    filename = models.FileField(upload_to='static/uploads/', max_length=128, default='default.pdf')

    def __str__(self):
        return "{}".format(self.title)
    
    