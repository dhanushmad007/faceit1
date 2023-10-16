from django.db import models

# Create your models here.
# models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='static/videos/')
