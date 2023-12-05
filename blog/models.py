from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ('fashion', 'FASHION'),
    ('clothes', 'CLOTHES'),
    ('shoes', 'SHOES'),
    ('electronics', 'ELECTRONICS'),
)

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICE, default='fashion')
    featured_image = models.ImageField(upload_to='blog_featured_image', blank=True)
    slug = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=50, default='')
    content = models.TextField()
    timestamp = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title