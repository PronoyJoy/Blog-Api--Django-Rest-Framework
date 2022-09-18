from optparse import Option
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="category_name",max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    class BlogPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'published')

    option = (
        ('draft','Draft'),
        ('published','Published')
    )
    category = models.ForeignKey(
        Category,on_delete = models.PROTECT, default = 1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=300,unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name="blog_posts")
    status = models.CharField(
        max_length=100, choices=option, default='published')

    objects = models.Manager() #default manager
    postobjects = BlogPostObjects() #custom manager

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title





