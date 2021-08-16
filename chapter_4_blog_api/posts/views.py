from django.contrib.auth import models
from rest_framework import permissions
from posts.serializers import UserSerializer, PostSerializer 
from posts.models import Post
from posts.permissions import isAuthorOrReadOnly, UserPermissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (isAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermissions, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer






