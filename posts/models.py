from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=120)
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=500, null=True, blank=True)
