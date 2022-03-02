from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import *

def home(request):
    posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date') # 날짜 기준 내림차순 정렬
    return render(request, 'index.html', {'posts': posts,})

# 글 작성 html을 보여주는 함수
def new(request):
    return render(request, "new.html")

# 작성한 글을 저장하는 함수
def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect("home")

def formcreate(request):
    if request.method == "POST":
        # 사용자가 입력한 내용을 db에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect("home")
    else: # request가 get 요청일 때
        # 입력을 받을 수 있는 html을 렌더링
        form = BlogForm()
    return render(request, "form_create.html", {"form": form, })

def modelformcreate(request):
    if request.method == "POST" or request.method == "FILES":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = BlogModelForm()
    return render(request, "form_create.html", {"form": form,})

def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'detail.html', context)

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)