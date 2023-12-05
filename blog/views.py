from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def blogIndex(request):
    allPosts = Post.objects.filter(published=True).order_by('-timestamp')

    context = {'allPosts': allPosts}
    return render(request, 'blog/blogtest.html', context)