
from django.urls import path
from phonebook import views

urlpatterns = [
    path('', views.test),
    path('index/', views.index),
    path('add/', views.add),
    path('delete/', views.delete),
    path('detail/<int:userId>/', views.detail),
    path('update/', views.update),
]

