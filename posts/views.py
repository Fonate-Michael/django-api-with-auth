from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .models import Post
from .serializers import PostSerializers


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
      
        if request.method in SAFE_METHODS:
            return True

       
        return obj.author == request.user


class PostViewList(generics.ListCreateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()



class PostViewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewUpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    lookup_field = 'pk'