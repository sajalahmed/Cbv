from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True)
    description = models.TextField()
    author = models.TextField(null=True)
    count = models.IntegerField(null=True, default=0)
    coverpage = models.FileField(null=True)
    
    def __str__(self):
        return self.title
        
    def get_title():
        return "abul Kashem" + title
