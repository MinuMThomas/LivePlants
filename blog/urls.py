from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.blog_list, name='blog_list')
    # path('blogs/', views.blog_list, name='blog_list'),
    # path('', views.BlogListView.as_view(), name='blog_list'),
    # path('<int:title_id>/', views.blog_detail, name='blog_detail'),
]
