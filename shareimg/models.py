from django.db import models

# Create your models here.

class SharedImage(models.Model):
    title = models.CharField(max_length = 600)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    
