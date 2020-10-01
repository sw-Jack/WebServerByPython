
from django.shortcuts import render
from phonebook.models import PhoneBook
# Create your views here.

def test(request) :
    return render(request, "test/test.html")

def index(request) :
    # PhoneBook 에 있는 값을 가져올 변수 alluser
    # PhoneBook 에 있는 값들 중 '이름', '전화번호'에 해당하는 정보들만 가져오겠다
    alluser = PhoneBook.objects.values('id','이름','전화번호')
    # 콘솔창 출력
    print(alluser)
    # 브라우저에 띄울 변수 (딕셔너리 형태)
    context = {"phonebook" : alluser}
    return render(request, "phonebook/index.html", context)

def add(request) :
    return render(request, "phonebook/add.html")

def delete(request) :
    return render(request, "phonebook/delete.html")

def detail(request, userId) :
    # 사용자 정보를 가져오는데, .get(id=userId), 
    # 즉 id가 사용자가 입력한 사용자에 대한  정보를 가져온다.
    alluser = PhoneBook.objects.values('id','이름','전화번호',
                                '주소','이메일','생년월일').get(id=userId)
    print(alluser)
    context = {"phonebook" : alluser}
    return render(request, "phonebook/detail.html", context)

def update(request) :
    return render(request, "phonebook/update.html")


