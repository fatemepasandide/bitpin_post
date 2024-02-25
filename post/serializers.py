from rest_framework import serializers

from post.models import Post, Score


class PostSerializer(serializers.ModelSerializer):
    score_average = serializers.JSONField(read_only=True)
    count_score = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'score_average',
            'count_score',
        ]


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = [
            'id',
            'score',
            'user',
            'post'
        ]
