from django.shortcuts import get_object_or_404, render
from .models import Post   
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404 

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog/home.html", {'posts': posts})        

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post}
    )          
    

def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm()

    return render(
        request,
        'blog/create_post.html',
        {'form': form}
    )

def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)

    else:
        form = PostForm(instance=post)

    return render(
        request,
        'blog/edit_post.html',
        {
            'form': form,
            'post': post
        }
    )
def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(
      request,
        'blog/delete_post.html',
        {'post': post}
    )
