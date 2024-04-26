from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import os


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    valid_posts = []
    for post in posts:
        if os.path.exists(post.image.path):
            valid_posts.append(post)
    return render(request, 'bulletin_board/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'bulletin_board/create_post.html', {'form': form})
