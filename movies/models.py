from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField("Movie", max_length=255)
    description= models.CharField("Movie desc", max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    

    def __str__(self):
        return self.name

