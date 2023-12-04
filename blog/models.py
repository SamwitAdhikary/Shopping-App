from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    featured_image = models.ImageField(upload_to='blog_featured_image', blank=True)
    slug = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=50, default='')
    content = models.TextField()
    timestamp = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title