from django.shortcuts import render, HttpResponse

def main(request) :
    return HttpResponse("main page")

def test(request) :
    context = {"key":"key에 대한 value 출력",
                "num":100,
                "float":123.123,
                "str":"문자열 저장",
                "list":[10,20,"리스트 저장"],
                "dictionary":{"a":"a 저장","b":"b 저장"}
                }
    return render(request, "myhtml/test.html", context)

def tempcode(request) :
    context = {
        "네이버":"https://www.naver.com",
        "구글":"https://www.google.com",
        "다음":"https://www.daum.net",
        "rank":[ [1,2,3,4,5], ['육','7','팔','구','10'], [11,12,13,14,15] ]
    }
    return render(request, "myhtml/tempcode.html", context)

def worldcup(request) :
    context = {
        "wcInfo" : [ ["순위","국가","승점","승","무","패","득점","실점","골득실"],
                    [1,{"이란":"https://www.naver.com"},17,5,2,0,6,0,6],
                    [2,{"대한민국":"https://www.google.com"},13,4,1,2,9,7,2],
                    [3,{"시리아":"https://www.daum.net"},8,2,2,3,2,3,-1] ]
    }
    return render(request, "myhtml/worldcup.html", context)

