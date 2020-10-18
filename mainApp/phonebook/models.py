from django.db import models

# Create your models here.

class PhoneBook(models.Model):
    이름 = models.CharField(max_length=50, null = False)
    전화번호 = models.CharField(max_length=20)
    이메일 = models.EmailField()
    주소 = models.CharField(max_length=200)
    생년월일 = models.DateField()
    작성자 = models.CharField(max_length=50, null = False)