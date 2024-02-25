from rest_framework import serializers

from post.models import Post, Score


class PostSerializer(serializers.ModelSerializer):
    score_average = serializers.JSONField(read_only=True)
    count_score = serializers.IntegerField(read_only=True)
    user_score = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'score_average',
            'count_score',
            'user_score',
        ]

    def get_user_score(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        if user.is_authenticated:
            return obj.user_score(user)
        return None


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = [
            'id',
            'score',
            'user',
            'post'
        ]
