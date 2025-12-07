from django.urls import path
from .views import PostViewCreate, PostViewUpdateDeleteRetrive, PostViewList

urlpatterns = [
    path('posts/', PostViewList.as_view(), name='list-post'),
    path('posts/create/', PostViewCreate.as_view(), name='create-post'),
    path('posts/<int:pk>/', PostViewUpdateDeleteRetrive.as_view(), name='update-delete-get-post'),
]