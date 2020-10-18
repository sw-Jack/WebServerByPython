from django.contrib import admin
from border.models import Border
# Register your models here.
class BorderView(admin.ModelAdmin):
    list_display=("id","제목","작성자","조회수")
admin.site.register(Border, BorderView)