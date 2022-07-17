from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.name

