from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    # primary key를 이용해 하나의 post검색
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html',{'post':post})