from rest_framework import generics, permissions
from .models import Post, User
from .serializers import PostSerializer, PostCreateSerializer

class PostListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # post needs to be attached to User
        serializer.save(user=self.request.user)