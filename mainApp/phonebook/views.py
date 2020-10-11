
from django.shortcuts import render, redirect
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
    # 로그인 되어 있지 않은 경우 URL 통해 접근할 시 로그인 페이지로 강제 이동
    if request.user.is_active != True :
        return redirect("login")
    if request.method == 'POST':    # 데이터가 존재하고 데이터 처리가 일어난 경우
        table = PhoneBook()
        table.이름 = request.POST.get("name")
        table.전화번호 = request.POST.get("phNum")
        table.이메일 = request.POST.get("email")
        table.주소 = request.POST.get("addr")
        table.생년월일 = request.POST.get("bir")
        # 유저에게 입력받지 않고 DB상으로만 현재 유저 아이디 저장
        table.작성자 = request.user.username
        table.save()
        # return render(request, "phonebook/index.html") # 새로 저장한 값도 넘겨줘야함
        return redirect("PB:index") # redirect 사용을 위해 django.shortcuts 에서 redirect import
    else :  # GET 방식이면 아래 주소로 넘기기, 데이터 없이 페이지만 요청한 경우
        return render(request, "phonebook/add.html")

def delete(request, userId) :
    dele = PhoneBook.objects.get(id=userId)
    dele.delete()
    return redirect("PB:index")
    # return render(request, "phonebook/delete.html")

def detail(request, userId) :
    # 사용자 정보를 가져오는데, .get(id=userId), 
    # 즉 id가 사용자가 입력한 사용자에 대한  정보를 가져온다.
    alluser = PhoneBook.objects.values('id','이름','전화번호',
                                '주소','이메일','생년월일','작성자').get(id=userId)
    print(alluser)
    context = {"phonebook" : alluser}
    return render(request, "phonebook/detail.html", context)

def update(request, userId) :
    table = PhoneBook.objects.get(id=userId)
    context = {"phonebook" : table}

    if request.method == 'POST' :
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('addr')
        table.생년월일 = request.POST.get('bir')
        table.save()
        return redirect("PB:detail", userId)
    else :
        if table.작성자 == request.user.username :
            return render(request, "phonebook/update.html", context)
        else : 
            return redirect("PB:index")


