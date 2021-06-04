from django import urls
from django.urls import path
from django.contrib import admin
from board.views import index, blog, posting

app_name='main'

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('blog/',blog, name='blog'),
    path('blog/<int:pk>/',posting),
]