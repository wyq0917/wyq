from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('ok')
from book.models import BookInfo,PeopleInfo
# BookInfo.objects.all()
# from book.models import BookInfo,PeopleInfo
from book.models import BookInfo
book=BookInfo(
    name='葵花宝典',
    pub_date='2020-1-2',
    readcount=100)

# 必须调用 对象的save方法 数据才会保存到数据中
"""
save方法的本质是 获取到对象的属性和属性值,调用ORM的数据保存方法
转换为一条sql语句,然后让mysql去执行
"""
# book.save()

# 方式2
# 数据可以直接保存
# objects 相当于模型的管理属性

book=BookInfo.objects.create(
    name='django',
    pub_date='2005-1-1',
    readcount=666,
    commentcount=999
)
