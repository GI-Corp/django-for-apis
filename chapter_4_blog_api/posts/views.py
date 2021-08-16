from django.contrib.auth import models
from django.shortcuts import render
from django.utils.functional import classproperty
from rest_framework import generics, permissions
from posts.serilaizers import PostSerializer
from posts.models import Post
from posts.permissions import isAuthorOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer




