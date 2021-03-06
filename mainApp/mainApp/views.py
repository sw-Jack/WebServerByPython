from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from border.models import Border

def createAccount(request):
    if request.method == "GET":
        return render(request,"registration/register.html")
    else:
        User.objects.create_user(
            username = request.POST.get("userId"),
            password = request.POST.get("userPassword"),
            first_name = request.POST.get("userFirstName"),
            last_name = request.POST.get("userLastName"),
            email = request.POST.get("userEmail")
        )
        return redirect("login")

def test(request):
    print('Get userId : ',request.GET.get('userId'))
    print('Get userPwd : ',request.GET.get('userPwd'))
    print("============================")
    print('POST userId : ',request.POST.get('userId'))
    print('POST userPwd : ',request.POST.get('userPwd'))
    return render(request,"test/test.html")

def mainIndex(request):
    #print("로그인한 사용자 : ", request.user.username )
    #print("로그인 확인 : ", request.user.is_active)
    return render(request,"mainapp/mainIndex.html")

def userInfo(request, userId):
    userInfo = User.objects.get(id = userId)
    print(userInfo)
    content = {"userInfo":userInfo}
    if request.method == 'GET':
        return render(request,"registration/userInfo.html",content)
    else:
        user = request.user
        user.username = request.POST.get('username')
        user.last_name = request.POST.get('last_name')
        user.first_name = request.POST.get('first_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('userInfo',request.user.id)

def img(request):
    return render(request,"test/img.html")

def page(request, num) :
    boardContext = Border.objects.all()
    paging = Paginator(boardContext, 2) # 한 페이지당 2개의 글을 보여주겠다.
    context = {"pageNum" : paging.page(num)}
    return render(request, "test/page.html", context)



'''
로그인한 사용자 : {{user.username}}<br>
로그인한 사용자 id : {{user.id}}<br>
로그인 확인 : {{user.is_active}}<br>
관리자인지 : {{user.is_superuser}}<br>
마지막 로그인 날짜 : {{user.last_login}}<br>
이름 : {{user.first_name}}<br>
성 : {{user.last_name}}<br>
이메일 : {{user.email}}<br>
'''
