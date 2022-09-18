from django.urls import path
from django.views.generic import TemplateView
from .views import PostDetail,PostList
app_name ="blog_api"

urlpatterns = [
    path('',PostList.as_view(), name='listview'),
    path('<int:pk>/',PostDetail.as_view(), name = "detailview")
]
