from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # pk stands for primary key (int: lets django know to only accept integers)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # create a post url pattern
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # update post url pattern
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # delete url pattern
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # delete url pattern
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]