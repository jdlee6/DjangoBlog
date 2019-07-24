from django.shortcuts import render
from .models import Post
# import ListView (showing blog posts on home page)
# import DetailView (details of a single post object)
# import CreateView (creating a post)
# import UpdateView (updating a post)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based view handle a lot more logic (different kinds: list views, detail views, create views, update views, delete views and etc.)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering =['-date_posted']


class PostDetailView(DetailView):
    model = Post
   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields we want when we create a post
    fields = ['title', 'content']

    def form_valid(self, form):
        # before you submit the form, take that instance and set the author equal to the current logged in user
        form.instance.author = self.request.user
        # then run the form_valid(form) method on our parent class
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # create a function that our UserPassesTestMixin will run in order to see if our user passes the test condition
    def test_func(self):
        # get the post with get_object() method
        post = self.get_object()
        # if current logged in user is the author of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})