# _*_ coding:utf-8 _*_
"""again URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pangle.views import index

urlpatterns = [
    url(r'^jijiaogala/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

# 404和500错误页面配置
handler404 = 'pangle.views.view_404'
handler500 = 'pangle.views.view_500'
