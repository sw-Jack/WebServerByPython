

from django.db import models

# Create your models here.
# class는 DB에서 하나의 테이블과 동일
# class 생성 과정은 DB에서의 테이블 생성 과정과 동일
# 즉, create table PhoneBook('이름' varchar(50) not null..) 과 동일

class PhoneBook(models.Model) :
    # CharField : 문자열
    # 이름은 문자열로 저장하는데, 최대 길이는 50이고 not null(무조건 값이 존재해야함)
    이름 = models.CharField(max_length=50, null=False)
    전화번호 = models.CharField(max_length=20)
    # EmailField : 이메일 형식
    이메일 = models.EmailField()
    주소 = models.CharField(max_length=200)
    # DateField : 날짜 형식
    생년월일 = models.DateField()
    작성자 = models.CharField(max_length=50, null=False)

    



    