from pyexpat import model
from .models import Post


from rest_framework import serializers



class PostSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('__all__')