from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializers
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    lookup_field = 'pk'