from django.db import models


# 将一个普通类变成可以映射到数据库中的ORM模型
# 那么必须将父类设置为models.Model或者他的子类
class Movie(models.Model):


    # id字段，自增长
    id = models.AutoField(primary_key=True)
    # name, varchar类型，长度100
    name = models.CharField(max_length=100, null=False)
    # author， varhcar类型
    author = models.CharField(max_length=100, null=False)
    # price, float类型
    price = models.FloatField(null=False, default=0)
