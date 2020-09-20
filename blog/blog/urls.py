"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    re_path(r'^blog/([0-9]{4})/([0-9]{2})/$', views.blog),
    re_path(r'^blogname/([a-zA-z]+)/$', views.blogName),
    re_path(r'^board/([0-9]+)', views.board),
    path('test/', views.test),


    # path('blog/2017', views.blog),
    # path('blog/2016', views.blog),
    # path('blog/2015', views.blog),

]
