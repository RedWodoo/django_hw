from django.db import models

# Create your models here.
class Bb(models.Model):
    content = models.TextField(null=True, blank=True)
