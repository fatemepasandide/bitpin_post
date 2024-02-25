from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    body = models.TextField(verbose_name='Body')

    @property
    def score_average(self) -> float:
        """
        :return: average score
        """
        return self.score_set.aggregate(Avg('score'))

    @property
    def count_score(self) -> int:
        return self.score_set.count()

    def __str__(self):
        return self.title

    def user_score(self, user):
        try:
            score = self.score_set.get(user=user)
            return score.score
        except Score.DoesNotExist:
            return None



class Score(models.Model):
    score = models.PositiveIntegerField(verbose_name='Score', validators=[MinValueValidator(0), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        unique_together = (('user', 'post'),)
