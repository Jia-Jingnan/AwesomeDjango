from django.db import models


# Create your models here.
# 一个类映射成一张表，一个对象映射成一条记录
class User(models.Model):
    # id int primary_key auto_increment
    id = models.AutoField(primary_key=True)
    # CharField必须指定max_length
    # verbose_name 字段注释，所有Field都有该属性
    username = models.CharField(max_length=255, verbose_name='yo')
    password = models.IntegerField()
    # 在表不为空的情况下添加字段
    age = models.IntegerField(verbose_name='年龄')
    # 声明字段可以为空
    info = models.CharField(max_length=255, null=True)
    # 声明字段的默认值
    hobby = models.CharField(max_length=255, default='study')


    # 打印对象时调用该方法,定义对象要显示的信息，相当于Java中的toString方法
    def __str__(self):
        return self.username


# 一对多或多对一时，关键字段建在多的一侧
# 多对多时，新建一张中间表，映射关系



# 数据库迁移命令

class Author(models.Model):
    # 由于一个表必须有一个主键，一般情况都命名为Id
    # django会自动创建一个id的主键字段
    username = models.CharField(max_length=255)
    password = models.IntegerField()

