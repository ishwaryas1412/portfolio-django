from django.db import models

# Create your models here.
class Myworks(models.Model):
    title =models.CharField(max_length=200)
    description=models.TextField()

    url =models.URLField(blank=True)
