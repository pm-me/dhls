# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

from DjangoUeditor.models import UEditorField       # 导入UEditorField字段，代替models.TextField字段

# Create your models here.


class Category(models.Model):
    """
    类别
    """
    item = models.CharField(verbose_name="类别", max_length=50)
    desc = models.CharField(verbose_name="描述", max_length=100)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.item


class Blog(models.Model):
    """
    blog
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    content = UEditorField(verbose_name="内容", width=700, height=200, default="",
                           imagePath="content/%(basename)s_%(datetime)s.%(extname)s",
                           filePath="content/%(basename)s_%(datetime)s.%(extname)s")
    category = models.ForeignKey(Category, verbose_name="类别")

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Download(models.Model):
    """
    download
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    content = models.TextField(verbose_name="正文")

    class Meta:
        verbose_name = "资源下载"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Friends(models.Model):
    """
    friends
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    content = models.TextField(verbose_name="正文")

    class Meta:
        verbose_name = "友情连接"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class About(models.Model):
    """
    about
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    content = models.TextField(verbose_name="正文")

    class Meta:
        verbose_name = "关于"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
