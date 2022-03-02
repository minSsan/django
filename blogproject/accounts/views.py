from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # post 요청 -> 로그인 처리
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    # get 요청 -> 로그인 폼을 담고 있는 html 파일을 렌더링

def logout(request):
    auth.logout(request)
    return redirect('home')