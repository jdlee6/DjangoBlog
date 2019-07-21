from django.shortcuts import render
# models is in the same directory which is why we can use .
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # if it is short enough we can just place it directly as an argument like so
    return render(request, 'blog/about.html', {'title': 'About'})