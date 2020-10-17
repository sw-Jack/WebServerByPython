
from django.shortcuts import render
from border.models import Border

def index(request) :
    userAll = Border.objects.values("id","제목","작성자","내용","조회수")
    context = {"userAll" : userAll}
    return render(request, "border/index.html", context)


