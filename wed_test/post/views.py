from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            photo = post_form.cleaned_data['photo']
            content = post_form.cleaned_data['content']
            Post.objects.create(title=title, photo=photo, content=content)
            return redirect('post_list')
    else:
        post_form = PostForm()
    context = {
        'post_form': post_form,
    }
    return render(request, 'post/post_create.html', context)

def post_delete(request, post_pk):
    if request.method == "POST":
        Post.objects.get(pk=post_pk).delete()
    return redirect('post_list')
