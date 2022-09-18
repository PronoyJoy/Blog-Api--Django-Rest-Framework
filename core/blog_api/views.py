
from ast import Pass
from msilib.schema import Class
from rest_framework import generics
from blog.models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = BlogPost.postobjects.all()
    serializer_class = BlogPostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer