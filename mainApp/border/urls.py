from django.urls import path
from border import views

app_name = "BD"

urlpatterns = [
    path('<int:pageNum>/', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('detail/<int:boardId>/', views.detail, name="detail"),
    path('delete/<int:boardId>/', views.delete, name="delete"),
    path('update/<int:boardId>/', views.update, name="update"),
]


