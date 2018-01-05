# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) #博客题目
    category = models.CharField(max_length=50, blank=True) #博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = models.TextField(blank=True, null=True) #博客文章正文

    # 如果没有定义这个方法就需要在views文件加上item_link方法
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    #python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title

# 按时间下载排序
class Meta:
    ordering = ['-date_time']


