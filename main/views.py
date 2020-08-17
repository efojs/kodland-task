from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogPost
from .forms import BlogPostForm

def root(request):
    posts = BlogPost.objects.all().order_by('-created_at')[:10]
    return render(
        request,
        'main/root.html',
        {'posts': posts},
    )

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(
        request,
        'main/blog_post.html',
        {'post': post},
    )

def new_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            print('')
            print(blog_post)
            print('')
            return redirect(
                'blog_post',
                post_id = blog_post.id,
            )
    else:
        form = BlogPostForm()

    return render(
        request,
        'main/new_blog_post.html',
        {'form': form},
    )
