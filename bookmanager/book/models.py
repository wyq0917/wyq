from django.db import models

# Create your models here.
'''
书籍表
id	name
1	西游记
2	三国演义
人物表
id	name	gender	book
1	孙悟空	False	1
2	白骨精	True	1
3	曹操	    False	2
4	貂蝉	    True	2
'''
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10)
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
