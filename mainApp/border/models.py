
from django.db import models

class Border(models.Model) :
    제목 = models.CharField(max_length=255, null = False)
    작성자 = models.CharField(max_length=255, null = False)
    내용 = models.TextField(null = False)
    작성일 = models.DateTimeField(null = False)
    수정일 = models.DateTimeField(null = False)
    조회수 = models.IntegerField(null = False)




