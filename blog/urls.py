from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # pk stands for primary key (int: lets django know to only accept integers)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # create a post url pattern
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # update post url pattern
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]