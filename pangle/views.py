# _*_ coding:utf8 _*_
from django.shortcuts import render, render_to_response

from models import Category, Blog, Download, Friends, About

# Create your views here.


def index(request):
    all_blog = Blog.objects.all()
    all_download = Download.objects.all()
    all_friends = Friends.objects.all()
    all_about = About.objects.all()
    return render(request, 'index.html', {"all_blog": all_blog, "all_download": all_download, "all_about": all_about,
                                          "all_friends": all_friends})


# 全局404处理函数
def view_404(request):
    response = render_to_response('404.html', {})  # 返回404页面
    response.status_code = 404  # 状态码为404
    return response


# 全局500处理函数
def view_500(request):
    response = render_to_response('500.html', {})  # 返回500页面
    response.status_code = 500  # 状态码为500
    return response
