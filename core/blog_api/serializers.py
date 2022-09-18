from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ( 'id', 'title', 'author', 'content', 'status')