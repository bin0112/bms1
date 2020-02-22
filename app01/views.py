# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect

from app01.models import Book,Publish,Author,AuthorDetail,Emp
# Create your views here.
import json


def addrecode(request):

    pub_obj = Publish.objects.filter(name='容姐出版社').first()

    #一对一数据添加方式：
    # Book.objects.create(
    #     title='财务通',
    #     price=100,
    #     pub_date='2020-01-01',
    #     # publish_id=1,
    #     publish=pub_obj
    # )


    # 多对多数据添加方式：


    book = Book.objects.create(
        title='财务通',
        price=230,
        pub_date='2020-01-01',
        publish_id=1,
        # publish=pub_obj
    )
    # 方式1
    # bin = Author.objects.filter(name='bin').first()
    # rong = Author.objects.filter(name='rong').first()
    # book.authors.add(bin,rong)

    # 方式2
    # book.authors.add(1,2)


    # 方式3  最常用的方式
    # book.authors.add(*[1,2])  #打散的语法

    #################
    # bin = Author.objects.filter(name='bin').first()
    # book = Book.objects.filter(nid=6).first()
    # # book.authors.remove(bin)
    # book.authors.clear()  #直接清空app01_book_authoers中 book_id = 6 的所有数据


    ######### 解除再解绑
    book = Book.objects.filter(nid=2).first()
    # book.authors.clear()
    # book.authors.add(1)

    # book.authors.set(1) #等同于上面两句

    return HttpResponse('执行OK')

def query(request):

    ############ 基于对象的跨表查询 ##############

    ######### 一对多查询  ##########
    '''
    正向查询：关联属性所在的表查询关联表记录
    反向查询：


         正向查询：按字段：book.publish
    Book ----------------------------> Publish
         <----------------------------
         反向查询：表名小写_set.all()：pub_obj.book_set.all() 是queryset数据类型


    :param request:
    :return:
    '''

    # 1 查询python 这本书的出版社的名字和邮箱
    # 方式1
    # book = Book.objects.filter(title='python').first()
    # pub_obj = Publish.objects.filter(nid=book.publish_id).first()
    # print(pub_obj.name)
    # print(pub_obj.email)

    # 方式2
    # book = Book.objects.filter(title='python').first()
    # print(book.publish) # 与book这本书关联的出版社对象，不用像pub_obj再查询一次
    # print(book.publish.name)
    # print(book.publish.email)


    # 2 查询rongjie 出版社的所有书籍的名称

    # pub_obj = Publish.objects.get(name='rongjie')
    # print(pub_obj.book_set.all()) #queryset
    # print(pub_obj.book_set.all().values('title'))   #queryset



    ######### 多对多查询  ##########

    '''
         正向查询：按字段：book.authors.all()
    Book -------------------------------------> Author
         <-------------------------------------
         反向查询：表名小写_set.all()：bin.book_set.all() 是queryset数据类型

    '''

    # 查询 python 书籍作者的年龄

    # book = Book.objects.filter(title='python').first()
    # ret = book.authors.all()  # 查询与这本书籍关联的所有作者的queryset的集合
    # ret1 = book.authors.all().values('age')
    # print(ret)
    # print(ret1)

    # 查询bin出版过的所有书籍

    # bin = Author.objects.filter(name='bin').first()
    # ret = bin.book_set.all()
    # print(ret)


    ######### 一对一查询  ##########

    '''
           正向查询：按字段：bin.ad
    Author -------------------------------------> AuthorDetail
           <-------------------------------------
           反向查询：按表名小写 ad.author 
    
    '''

    # 查询bin 的手机号
    # bin = Author.objects.filter(name='bin').first()
    # ret = bin.ad.tel
    # print(ret)

    # 查询手机号是10000 的作者名字

    ad = AuthorDetail.objects.filter(tel=10000).first()
    print(ad.author.name)

    return HttpResponse('查询成功')



##################### 图书管理系统   视图函数 ##################

def book_view(request):

    book_list = Book.objects.all()

    return render(request,'book_view.html',{'book_list' : book_list})


def book_add(request):
    if request.method=='GET':
        publish_list = Publish.objects.all()
        author_list  = Author.objects.all()
        return render(request,'book_add.html',{'publish_list':publish_list,'author_list':author_list})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.getlist('authors') # 如果返回值是多个值的时候要使用getlist
        print(request.POST)

        book = Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        # django 中会转换数字字符串给数字
        book.authors.add(*authors) #列表通过*authors 打散




        return redirect('/books/')

def book_edit(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method =='GET':

        edit_book = Book.objects.filter(pk=edit_book_id).first()
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'book_edit.html',{'edit_book':edit_book,'publish_list':publish_list,'author_list':author_list})

    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        authors = request.POST.getlist('authors')  # 如果返回值是多个值的时候要使用getlist
        print(request.POST)


        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        # update 只会返回更新的条数
        edit_book.authors.set(authors) #set函数列表传进来不用加*，不用打散

        return redirect('/books/')

def book_del(request,del_book_id):

    Book.objects.filter(pk=del_book_id).delete()
    return redirect('/books/')


def query2(request):

    ############### 基于双下划线的跨表查询（基于join实现的） #######################
    # Key : 正向查询按字段，反向查询按表名小写


    # 1 查询python 这本书的出版社的名字和邮箱
    # ret = Book.objects.filter(price="1111").values("publish__name") # 正向查询直接是字段
    # print(ret)
    #
    # ret1 = Publish.objects.filter(book__title='python').values('name')  # 反查：Book表小写book加双下划线加字段
    # print(ret1)

    # 2 查询rongjie 出版社的所有书籍的名称

    # ret = Publish.objects.filter(name='rongjie').values('book__title')
    # print(ret)

    # ret = Book.objects.filter(publish__name='rongjie').values('title')
    # print(ret)


    # 3 查询 python 书籍作者的年龄

    # ret = Book.objects.filter(title='python').values('authors__age')
    # print(ret)

    # ret = Author.objects.filter(book__title='python').values('age')
    # print(ret)

    # 4 查询bin出版过的所有书籍

    # 5 查询bin 的手机号

    # 6 查询手机号是10000 的作者名字


    ############# 连续跨表 ###################

    # 查询binge出版社出版过的所有书籍的名字以及作者的姓名

    # ret = Publish.objects.filter(name='binge').values('book__title','book__authors__name')
    # ret = Book.objects.filter(publish__name='binge').values('title','authors__name')
    # ret = Book.objects.filter().values('title','authors__name')
    # print(ret)


    # 查询手机号以100开头的作者出版过的所有书籍名称以及出版社名称

    # ret = Author.objects.filter(ad__tel__startswith=100).values('book__title','book__publish__name')
    # ret = Author.objects.filter(ad__tel__startswith=100).values_list('book__title','book__publish__name')
    # ret = AuthorDetail.objects.filter(tel__startswith='100').values_list('author__book__title',
    #                                                                      'author__book__publish__name'
    #                                                                      )
    # print(ret)

    ############### 聚合  分组 ###################


    # 聚合
    from django.db.models import Avg,Max,Sum,Min,Count
    #
    # # ret = Book.objects.all().aggregate(Avg('price'))
    # ret = Book.objects.aggregate(priceAvg=Avg('price'))  # 可以自主命名，可以把.all()去掉
    # ret = Book.objects.all().aggregate(c=Count(1))
    #
    # print(ret)


    # 分组
    # 单表分组查询
    # 查询每个出版社ID对应书籍个数
    # key：annotate()前select哪一个字段就按哪个字段group by ,annotate()的()中是添加分组的功能     annotate() = group by
    # ret = Book.objects.values('publish_id').annotate(c=Count(1)) # 分组需要设置别名，此行别名是 c

    # 查询每个部门的名称以及对应员工的平均薪水
    # ret = Emp.objects.values('dep').annotate(avg_salary=Avg('salary'))

    # 查询每一个省份的名称以及对应的员工的最大年龄
    # ret = Emp.objects.values('pro').annotate(max_age=Max('age'))
    # print(ret)

    # 跨表分组查询
    # 查询每一个出版社的名称以及对应书籍的个数
    # 方式一
    # ret = Book.objects.values('publish__name').annotate(c=Count(1))
    # 方式二
    # ret = Publish.objects.values('name').annotate(c=Count('book__title'))
    # ret = Publish.objects.values('name','email').annotate(c=Count('book__title'))  # 按多个栏位分组

    # 查询每个作者的名字以及出版书籍的最高价格
    # ret = Book.objects.values('authors__nid','authors__name').annotate(max_price=Max('price'))

    # 查询每一个书籍名称对应的作者个数
    # ret = Book.objects.values('pk','title').annotate(c=Count('authors__nid'))


    # 最常用方式
    # ret = Publish.objects.all().annotate(avg_price=Avg('book__price')).values('name','avg_price')
    # 将整体Publish进行分组，并将分组的新内容进行添加至Queryset对象中，数据可以调用

    # ret = Author.objects.annotate(max_price=Max('book__price')).values('name','max_price')

    # 查询作者数不止一个的书籍名称及作者个数
    # ret = Book.objects.annotate(c=Count("authors")).filter(c__gt=1).values('title','c')

    # print(ret)


    ############ F 与 Q #########################
    from django.db.models import F,Q

    # F 函数是获取栏位值

    # 查询评论数大于100的所有书籍名称

    # ret = Book.objects.filter(comment_count__gt=100).values('title')

    # 查询评论数大于点赞数的所有书籍名称

    # ret = Book.objects.filter(comment_count__gt=F('poll_count')).values('title')

    # 查询评论数大于两倍点赞数的所有书籍名称

    # ret = Book.objects.filter(comment_count__gt=F('poll_count')*2).values('title')

    # 给每一本书籍的价格提高100

    # ret = Book.objects.all().update(price=100+F('price'))

    # print(ret)


    # Q 函数 : 条件合并，并增加查询条件 与、或、非


    # 且是直接在filter中加逗号就好
    # 查询书本价格大于300且评论数大于2000的书籍
    # ret = Book.objects.filter(price__gt=300,comment_count__gt=2000)

    # 查询书本价格大于300或者评论数大于2000的书籍

    # 与 &      或 |     非 ~
    # ret = Book.objects.filter(Q(price__gt=300)|~Q(comment_count__gt=3000))


    ret = Book.objects.filter(Q(Q(price__gt=300) | Q(comment_count__gt=2000))&~Q(poll_count__gt=2000))


    print(ret)

    return HttpResponse("查询成功")

def book_ajax_del(request,del_book_id):
    response = {"state": True}
    try:
        Book.objects.filter(pk=del_book_id).delete()
    except Exception as e:
        response = {"state": False}

    return HttpResponse(json.dumps(response))
