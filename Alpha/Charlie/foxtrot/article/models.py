from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 定义字段时如果没有执行null=True,默认情况下null=False，即不能为空
    removed = models.NullBooleanField()
    # 如果charFiled超过256个字符不推荐使用CharFiled，推荐使用TextFeild，可以存储文本
    title = models.CharField(max_length=200)