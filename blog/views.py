from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, per_page=5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

