from rest_framework import generics

from post.models import Post, Score
from post.serializers import PostSerializer, ScoreSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ScoreListView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreUpdateView(generics.UpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
