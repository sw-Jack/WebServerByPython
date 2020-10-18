from django.shortcuts import render,redirect
from border.models import Border
from datetime import datetime
from django.core.paginator import Paginator

def index(request, pageNum):
    userAll = Border.objects.values("id","제목","작성자","내용","조회수").order_by('-id')
    paging = Paginator(userAll, 4) # 한 페이지 4개의 글을 보여줌
    print("paging.num_pages : ", paging.num_pages)
    arrPage = []
    for i in range(paging.num_pages) :
        print("i : ", i)
        arrPage.append(i+1)
    context = {"userAll":paging.page(pageNum), "arrPage":arrPage}
    return render(request,"border/index.html",context)

def add(request):
    if request.method == "POST":
        table = Border()
        table.제목 = request.POST.get("title")
        table.내용 = request.POST.get("context")
       
        table.작성자 = request.user.username
        table.작성일 = datetime.now()
        table.수정일 = datetime.now()
        table.조회수 = "0"
        #table.작성자 = request.POST.get("author")
        #table.작성일 = request.POST.get("cdate")
        #table.수정일 = request.POST.get("udate")
        #table.조회수 = request.POST.get("vcount")
        table.save()
        return redirect("BD:index")
    else:
        return render(request,"border/add.html")

def detail(request, boardId):
    borderCnt = Border.objects.get(id=boardId)
    borderCnt.조회수 = borderCnt.조회수 + 1
    borderCnt.save()
    borderTable = Border.objects.values("id",
                "제목","작성자","조회수","수정일","작성일","내용").get(id=boardId)
    return render(request,"border/detail.html",{"border":borderTable})

def delete(request, boardId) :
    dele = Border.objects.get(id=boardId)
    dele.delete()
    return redirect("BD:index")

def update(request, boardId) :
    boardInfo = Border.objects.get(id=boardId)
    if request.method == "POST" :
        boardInfo.제목 = request.POST.get('title') 
        boardInfo.내용 = request.POST.get('context')
        boardInfo.수정일 = datetime.now()
        boardInfo.save()
        return redirect("BD:detail", boardInfo.id)
    else :
        return render(request, "border/update.html", {"border":boardInfo})