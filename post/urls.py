from rest_framework import routers
from django.urls import path

from post import views

router = routers.SimpleRouter()
urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('score/', views.ScoreListView.as_view()),
    path('score-update/<int:pk>/', views.ScoreUpdateView.as_view()),
]
urlpatterns += router.urls
