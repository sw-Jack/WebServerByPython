from django.urls import path
from phonebook import views
app_name = "PB"
urlpatterns = [
    path('', views.test),
    path('add/', views.add , name = "add"),
    path('delete/<int:userId>/', views.delete, name="delete"),
    path('detail/<int:userId>/', views.detail, name = "detail"),
    path('index/', views.index, name = "index"),
    path('update/<int:userId>/', views.update, name ="update"),
]