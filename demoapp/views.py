from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def summary(request):
    return render(request, 'demoapp/summary.html')

def installation(request):
    return render(request, 'demoapp/installation.html')

def tutorial(request):
    return render(request, 'demoapp/tutorial.html')

def conclusions(request):
    return render(request, 'demoapp/conclusions.html')

def credits(request):
    return render(request, 'demoapp/credits.html')

def page4(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)

        if form.is_valid():
            form.save()
            posts = Post.objects.all()
            messages.success(request, ('Post made successfully!'))
            return render(request, 'demoapp/page4.html', {'posts': posts})
    else:
        posts = Post.objects.all()
        return render(request, 'demoapp/page4.html', {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, ('Post has been deleted successfully!'))
    return redirect('page4')

def edit(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = PostForm(request.POST or None, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, ('Post has been edited successfully!'))
            return redirect('page4')
    else:
        post = Post.objects.get(id=post_id)
        return render(request, 'demoapp/edit.html', {'post': post})