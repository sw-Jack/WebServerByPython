
from django.urls import path
from border import views

app_name = "BD"
urlpatterns = [
    path('', views.index, name="index"),
]


