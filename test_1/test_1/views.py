#from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def main(request) :
    return HttpResponse("메인페이지")

def test(request) :
    print("test입니다")
    return render(request, "test.html")
#   return HttpResponse('결과 값을 돌려줍니다')



