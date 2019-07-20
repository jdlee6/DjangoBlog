from django.shortcuts import render

# create dummy data, posts
posts = [
    {
            'author': 'CoreyMS',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # if it is short enough we can just place it directly as an argument like so
    return render(request, 'blog/about.html', {'title': 'About'})