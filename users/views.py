from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import User

# Create your view here.


def join_up(request):
    if request.method == 'GET':
        return render(request, 'joinup.html')
   # 메소드가 POST 정보저장
    elif request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       password2 = request.POST.get('password2')
       if password == password2:
            User.objects.create_user(username=username, password=password)
            return render(request, 'logon.html')
       else:
          return HttpResponse("비밀번호 확인 틀렸습니다.")
    else:
        return HttpResponse ("잘못된 접근 입니다.")
    
    
    
def log_on(request):
    return HttpResponse ("로그인 완료")
    