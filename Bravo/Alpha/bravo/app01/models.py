from django.db import models

# Create your models here.
# 创建表关系，先将基表创建出来，然后添加外键字段
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # 总共8位，小数点后占两位
    # 图书和出版社多对一的关系，书是多的一侧，外键放在book表
    publish = models.ForeignKey(to='Publish') # 默认就是与出版社表的主键字段做外键关联
    # 如果字段对应的事ForeignKey,那么orm或自动的在字段后面加上_id
    # 如果本身已经加了_id,orm仍然会加上_id

    # 图书和作者是多对多的关系，外键字段建在任何一方均可，建议建在查询频率较高的一方
    authors = models.ManyToManyField(to='Author')
    # authors 是一个虚拟字段，主要是告诉orm，book和author是多对多的关系
    # 让orm自动帮你创建第三张表


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # Author于AuthorDetial是一对一关系，外键建在任何一方均可，建议建在查询频率较高的一方
    author_detail = models.OneToOneField(to='AuthorDetail')
    # onetoonefield也会自动给字段加上_id


class AuthorDetail(models.Model):
    phone = models.BigIntegerField() # 或者直接使用字符类型
    addr = models.CharField(max_length=32)