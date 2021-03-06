from django.shortcuts import render
from .models import Post
posts = [
    {
        'author': 'JonM',
        'title': 'Post 1',
        'content': 'first post content',
        'date': '07/04/2021'
    },
    {
        'author': 'ElisaS',
        'title': 'Post 2',
        'content': 'second post content',
        'date': '07/05/2021'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About" })
