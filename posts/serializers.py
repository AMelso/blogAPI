from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "thumbnail",
        )

class PostUpdateSerializer(serializers.ModelSerializer):
    #don't require all fields to be changed, can leave some as they are.
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "thumbnail",
        )

