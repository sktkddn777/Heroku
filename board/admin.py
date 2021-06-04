from django.contrib import admin
# Post Model을 불러온다
from .models import Post
# Register your models here.

# admin이 Post에 접근 가능.
admin.site.register(Post)