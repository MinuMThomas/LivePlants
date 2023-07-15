from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog_list(request):
    """ Shows all blogs """

    blog = Blog.objects.all()

    context = {
        'blogs': blog,
    }

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_id):
    """ Shows individual blog details """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)
