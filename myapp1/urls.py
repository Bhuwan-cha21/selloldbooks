from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login_user, name ='login_user'),
    path('logout',views.logout_user, name="logout_user"),
    path('post_blog',views.post_blog, name="post_blog"),
    path('blog_detail/<int:id>',views.blog_detail, name="blog_detail"),
    path('blog_detail/blog_delete/<int:id>',views.blog_delete, name="blog_delete"),
    path('blog_detail/blog_edit/<int:id>',views.blog_edit, name="blog_edit")
]
