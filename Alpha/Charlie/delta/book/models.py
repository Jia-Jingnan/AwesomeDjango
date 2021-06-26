from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)

    # 重写book的str方法，相当于Java中的toString方法
    def __str__(self):
        return 'Book:[{}, {}, {}]'.format(self.name, self.author, self.price)