from django.urls import path, include
from .views import PostsView, IndexView

app_name = 'core'

urlpatterns = [
    path('posts', PostsView.as_view()),
    path('', IndexView.as_view()),
]