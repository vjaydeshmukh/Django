from django.contrib import admin
from django.urls import path
from blog.views import home, post_page,all_posts, create_post, delete_post, edit_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    # path('greet/<str:name>/', greet),
    path('post/<int:post_id>/',post_page),
    path('allposts/',all_posts),
    path('create/',create_post),
    path('delete/<int:post_id>/', delete_post),
    path('edit/<int:post_id>/', edit_post)
]
