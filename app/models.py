from django.db import models

# Create your models here.

class Sound(models.Model):
    name = models.CharField(null=True, blank=False, max_length=50)
    files = models.FileField(null=True, blank=True, upload_to='static/sounds/')

    def __str__(self):
        return self.name
