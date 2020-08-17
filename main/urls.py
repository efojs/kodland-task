from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('new/', views.new_blog_post, name='new_blog_post'),
    path('<int:post_id>/', views.blog_post, name='blog_post'),
]
