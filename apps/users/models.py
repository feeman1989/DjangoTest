# －*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from random import choice
# Create your models here.
class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male",u"男"),
        ("female",u"女"))
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(
        max_length=20,
        verbose_name=u"姓别",
        choices=GENDER_CHOICES,
        default="female")
    address = models.CharField(max_length=100, verbose_name=u"地址", default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    #image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100) 这个功能 暂时无法解决
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.username 

# 邮箱验证码模型
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register",u"注册"),
        ("forget",u"找回密码"))
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name 
        
# 轮播图模型
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
        
    