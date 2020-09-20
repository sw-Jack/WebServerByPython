

from django.http import HttpResponse
from django.shortcuts import render

def main(request) :
    return HttpResponse("메인 페이지")

def blog(request, year, month) :
    print("blog url 연결")
    return HttpResponse(year + "년" + month + "월 " + "blog url 연결")  

def blogName(request, guest) :
    print("blog url 연결")
    return HttpResponse(guest + "님 접속했습니다.")

def board(request, num) :
    return HttpResponse("{} 님 게시글 연결".format(num))

def test(request) :
    return render(request, "myhtml/test.html")

