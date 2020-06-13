from django.shortcuts import render

fake_posts = [
    {
        'author': 'Rich',
        'title': 'First Post',
        'content': 'This is harder than I thought.',
        'date_posted': '06/12/2020',
    },
    {
        'author': 'Not Rich',
        'title': 'Second Post',
        'content': 'This is much harder than I thought.',
        'date_posted': '06/12/2025',
    },
]

def home(request):
    context = {
        'posts': fake_posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
