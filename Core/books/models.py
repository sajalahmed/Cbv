from django.db import models
from django.template.defaultfilters import slugify

class Book(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True)
    description = models.TextField()
    author = models.TextField(null=True)
    count = models.IntegerField(null=True, default=0)
    coverpage = models.FileField(null=True, upload_to = "coverpage/")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_title(self):
        return "abul Kashem" + self.title
