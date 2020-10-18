from django.shortcuts import render , redirect
from phonebook.models import PhoneBook
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request,"test/test.html")
def add(request):
    print("통신 방식 : ",request.method)
    #if request.user.is_active != True:
    #    return redirect("login")
    if request.method == 'POST':
        table = PhoneBook()
        table.이름 = request.POST.get("name")
        table.전화번호 = request.POST.get("phNum")
        table.이메일 = request.POST.get("email")
        table.주소 = request.POST.get("addr")
        table.생년월일 = request.POST.get("bir")
        table.작성자 = request.user.username
        table.save()
        return redirect("PB:index")
    else:
        return render(request,"phonebook/add.html")


def delete(request , userId):
    dele = PhoneBook.objects.get(id = userId)
    dele.delete()
    return redirect("PB:index")
    #return render(request,"phonebook/delete.html")
def detail(request, userId):
    alluser = PhoneBook.objects.values('id','이름','전화번호',
                        '주소','이메일','생년월일','작성자').get(id = userId)
    print(alluser)
    context = {"phonebook":alluser}
    return render(request,"phonebook/detail.html",context)
def index(request):
    alluser = PhoneBook.objects.values('id','이름','전화번호')
    print(alluser)
    context = { "phonebook" : alluser }
    return render(request,"phonebook/index.html",context)
def update(request , userId):
    st='<script>alert("작성자와 일치하지 않습니다");location.href=\"{% url \"PB:index\" %}\"</script>'


    #if request.user.is_active != True:
    #    return redirect("login")
    table = PhoneBook.objects.get(id = userId)
    print("table : ",table)
    print("이름 : ",table.이름)
    context = {"phonebook": table}

    if request.method == 'POST':
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('addr')
        table.생년월일 = request.POST.get('bir')
        table.save()
        return redirect("PB:detail", userId)
    else:
        #return render(request,"phonebook/update.html",context)
        if table.작성자 == request.user.username:
            return render(request,"phonebook/update.html",context)
        else:
            return redirect("PB:index")

