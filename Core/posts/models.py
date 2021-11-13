from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name