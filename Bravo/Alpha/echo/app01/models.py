from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    register_time = models.DateField()  # 日期字段，表示年月日

    '''
    DateField
    DateTimeField
        两个重要参数：
        auto_now:每次操作数据的时候该字段会 自动将当前时间更新
        auto_now_add:在创建数据的时候会自动将当前创建时间记录下来，之后只要不认为的修改都不会变
    '''
    def __str__(self):
        return '对象：%s'%self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    # 库存
    inventory = models.IntegerField(default=1000)
    # 已卖数
    sold = models.IntegerField(default=1000)



    # Book 和 Publish是多对一的关系，外键建在多的一侧，即在Book上
    publish = models.ForeignKey(to='Publish')

    # Book 和 Author 是多对多的关系
    authors = models.ManyToManyField(to='Author')


    def __str__(self):
        return self.title



class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.EmailField() # 本质还是varchar，可以用来校验是否为邮箱格式

    def __str__(self):
        return '对象：%s'%self.name

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # Author 和 AuthorDetail 是一对一
    author_detail = models.OneToOneField(to='AuthorDetail')


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 电话
    addr = models.CharField(max_length=32)



# 自定义数据类型
class MyCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        # 调用父类的init方法
        super.__init__(max_length=max_length, *args, **kwargs)


    def db_type(self, connection):
        """
        返回真正的数据类型及各种约束条件
        :param connection:
        :return:
        """
        return 'char(%s)'%self.max_length