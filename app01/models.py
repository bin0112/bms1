# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    pub_date = models.DateTimeField() #"2012-12-12"
    comment_count=models.IntegerField(default=100)
    poll_count=models.IntegerField(default=100)
    publish = models.ForeignKey(to='Publish',on_delete=models.CASCADE,null=True)  # 级联删除 设置外键时可以增加null=True，可以默认此字段为空
    authors = models.ManyToManyField(to='Author') #多对多自行创建一张表的语句

    def __str__(self):
        return self.title


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    def __str__(self):
        return self.name






class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)
    # ad = models.ForeignKey('AuthorDetail',on_delete=models.CASCADE,unique=True)
    ad = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE) #同上，一样的结果
    def __str__(self):
        return self.name



class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()
    def __str__(self):
        return self.addr


class Author2Book(models.Model):
    nid = models.AutoField(primary_key=True)
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)


###########

class Emp(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)
    dep=models.CharField(max_length=32)
    pro=models.CharField(max_length=32)
    salary=models.DecimalField(max_digits=8,decimal_places=2)
