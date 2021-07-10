from django.test import TestCase


# Create your tests here.
# Model Test
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "echo.settings")
    import django
    django.setup()

    # 测试代码
    from app01 import models
    import datetime
    # 增
    # reg_date = datetime.datetime.now()
    # user = models.User.objects.create(name='stranger', age=1290, register_time=reg_date)
    # print(user)
    # import datetime
    # create_time = datetime.datetime.now()
    # 增，通过创建对象
    # user_obj = models.User(name='hulk', age=40, register_time=create_time)
    # user_obj.save()
    # print(user_obj)

    # 删除, pk会自动查找到当前表的主键字段，指代的是当前表的主键字段
    # 使用pk就不需要知道当前主键的名字了，不管是id,uid，tid都可以用pk代替
    # res = models.User.objects.filter(pk=1).delete()
    # print(res)
    # 删除方式二：现获取用户对象
    # user_obj = models.User.objects.filter(pk=2).first()
    # user_obj.delete()


    # 修改方式一
    # models.User.objects.filter(pk=8).update(name='doctor stranger')
    # get返回的直接就是当前数据对象，但是该方法不推荐使用，一旦数据不存在，该方法会直接报错
    # 还是使用filter
    # user_obj = models.User.objects.get(pk=9)
    # user_obj.name = 'tony stark'
    # user_obj.save()
    # print(user_obj)

    # 必知必会13条
    # 1.all(), 查询所有数据,QuerySet对象，列表嵌套字典
    # 2.fiter(), 带有过滤条件的查询,QuerySet对象，列表嵌套字典
    # 3.get(), 直接获取数据对象，但是条件不存在直接报错, 返回数据对象，非QuerySet对象
    # users = models.User.objects.get(pk=1)
    # print(type(users))
    # print(users)
    # 4.first(), 拿queryset的第一个数据
    # res = models.User.objects.all().first()
    # print(res)
    # 5.last()， 拿Query Set的最后一个对象
    # res = models.User.objects.all().last()
    # print(res)
    # 6.values(),重要
    # 需求，只想获取部分字段,可以指定要获取那些字段，返回结果是列表套字典，返回结果中会带有字段的属性名和属性值，key value形式
    # <QuerySet [{'name': 'God of Thunder', 'age': 1300}, {'name': 'God of mischeif', 'age': 1290}]>
    # res = models.User.objects.values('name', 'age')
    # print(res)
    # 7.values_list()，也可以指定要获取的字段, 返回值为列表套元组，返回结果中只有属性值没有属性名
    # <QuerySet [('God of Thunder', 1300), ('God of mischeif', 1290)]>
    # res = models.User.objects.values_list('name', 'age')
    # 查看内部的sql语句,这种查看SQL语句的方式只能用于queryset
    # print(res)

    # 8.distinct(), 不要在包含主键的时候做distinct，主键一定是不同的，
    # 去重一定要是一模一样的数据，主键不能忽略
    # res = models.User.objects.values('name', 'age').distinct()
    # print(res)

    # 9.order_by(), 默认升序排列
    # res = models.User.objects.order_by('age').values('age')
    # print(res)
    # 要排列的字段前加-可以实现降序排列
    # res = models.User.objects.order_by('-age').values('age')
    # print(res)

    # 10.reverse()， 翻转的前提是，数据已经排序，
    # res = models.User.objects.order_by('age').values('age')
    # res_1 = models.User.objects.order_by('age').values('age').reverse()
    # print(res)
    # print(res_1)

    # 11.count(), 统计当前数据的个数
    # res = models.User.objects.count()
    # print(res)
    # 12.exclude(), 不包含某个数据
    # res = models.User.objects.exclude(name='sif')
    # print(res)
    # 13.exists(),是否存在,返回True 或 FALSE，布尔值， 基本用不到
    # res =models.User.objects.filter(pk=3).exists()
    # print(res)

    # 神奇的双下划綫查询
    # 1.年龄大于1300岁的数据,gt=大于，gte=大于等于，lt=小于，lte=小于等于
    # res = models.User.objects.filter(age__gte=1300)
    # print(res)
    # 查询年龄或者1300，或者1400
    # res = models.User.objects.filter(age__in=[1300,1400])
    # print(res)
    # 查询年龄区间1300-1400, 顾头也顾尾
    # res = models.User.objects.filter(age__range=[1300,1400])
    # print(res)
    # 查询出名字里面含有o数据，模糊查询,属性是否包含
    # res = models.User.objects.filter(name__contains='o')
    # print(res)

    # 默认区分大小写
    # res = models.User.objects.filter(name__contains='O')
    # print(res)

    # 忽略大小写
    # res = models.User.objects.filter(name__icontains='O')
    # print(res)

    # 以...开头
    # res = models.User.objects.filter(name__istartswith='G')
    # print(res)

    # 以...结尾，增加i表示忽略大小写
    # res = models.User.objects.filter(name__iendswith='r')
    # print(res)

    # 查询出注册时间是2021年7月份的数据，只考虑月份，不考虑日
    # res = models.User.objects.filter(register_time__month='1')
    # print(res)

    # 按照年份查询
    # res = models.User.objects.filter(register_time__year='2021')
    # print(res)

    # and条件查询
    # res = models.User.objects.filter(register_time__year='2021', register_time__month='7')
    # print(res)


    # 一对多外键增删改查
    # 数据增
    # models.Book.objects.create(title='哈哈哈', price=133.22, publish_id=2)
    # 查询出一个出版社对象
    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.create(title='嘻嘻有机', price=12.2, publish=publish_obj)

    # 删除
    # models.Book.objects.filter(pk=15).delete()

    # 修改
    # models.Book.objects.filter(pk=1).update(publish_id=2)
    # 通过对象修改
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.filter(pk=1).update(publish=publish_obj)


    # 多对多增删改查,就是在操作第三张表
    # 如何给书籍添加作者
    # 先获取一个Book对象
    # 通过主键添加
    # book_obj = models.Book.objects.filter(pk=8).first()
    # print(book_obj.authors) # 就类似于已经找到了第三张表
    # book_obj.authors.add(3) # Book模型中有authors属性，给书籍对象绑定一个id为1的作者
    # book_obj.authors.add(2,3)

    # 通过对象添加
    # author_obj_1 = models.Author.objects.filter(pk=1).first()
    # author_obj_2 = models.Author.objects.filter(pk=2).first()
    # author_obj_3 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.add(author_obj_1)
    # book_obj.authors.add(author_obj_3, author_obj_2)
    # 括号内即支持添加数据也支持添加对象，都支持多个

    # 删,支持删除多个对象和数字，支持通过对象和主键删除
    # book_obj.authors.remove(2)
    # author_obj_1 = models.Author.objects.filter(pk=1).first()

    # 修改,先删除后新增
    # book_obj.authors.set([2]) # 括号内必须要一个可迭代对象

    # 在第三张表中清空某个数据与作者的绑定关系
    # 括号内不用加任何参数
    # book_obj.authors.clear()


    # 多表查询
    # 正反向的概念
    # 正向：由Book查询Publish是正向，外键字段在Book上，从多的查询少的，外键一般建议建在常用查询的表上
    # 反向：Publish没有外键字段，有Publish查Book就是反向

    # 正向查询按字段
    # 反向查询按表名小写

    # 子查询(基于对象的跨表查询)，分布操作
    # 1.查询数据主键为1的出版社名称，_set
    # book_obj = models.Book.objects.filter(pk=1).first()
    # 由书查出版社，正向查询，正向查询按字段，publish字段
    # res = book_obj.publish
    # print(res)
    # 获取书的名字
    # print(res.name)
    # print(res.addr)

    # 2.查询书籍主键为1的作者
    # 书查作者，外键在书，正向，按照字段查询
    # book_obj = models.Book.objects.filter(pk=1).first()
    # 多对多时使用all()
    # 什么时候使用.all(), 当有多个的时候，如果是1个则直接拿到对象
    # res = book_obj.authors.all()
    # print(res)

    # 3.查询作者jason的年龄
    # author_obj = models.Author.objects.filter(name='jason').first()
    # 正向查询按照字段，外键在
    # res = author_obj.author_detail
    # print(res)
    # print(res.phone)
    # 写orm语句时和写sql语句是一样的，不要企图一次性写完
    # 查询出版社是东方出版社出版的书
    # 先拿到出版社
    # publish_obj = models.Publish.objects.filter(name='东方出版社').first()
    # 出版社查书，反向查询，通过表名小写_set,有多个就使用.all()
    # res = publish_obj.book_set.all()
    # print(res)

    # 查询作者jason写过的书
    # author_obj = models.Author.objects.filter(name='jason').first()
    # 作者查书，反向，表名小写_set.all()
    # res = author_obj.book_set.all().first()
    # print(res.title)

    # 手机号是110的作者姓名
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
    # res = author_detail_obj.author
    # print(res.name)

    # 什么时候需要_set，当查询结果可以有多个的时候，必须要_set.all()
    # 当结果只有一个的时候不需要_set.all()


    # 联表查询(基于双下划线的跨表查询)
    # 查询书籍主键为1的出版社名称，一行代码搞定
    # 查询jason的手机号
    # res = models.Author.objects.filter(name='jason').values('author_detail__phone')
    # print(res)
    # res = models.Author.objects.filter(book__pk=1).values('name', 'book__title')
    # print(res)

    # 查询书籍主键为1的出版社名称和书的名称
    # res = models.Book.objects.filter(pk=1).values('title', 'publish__name')
    # print(res)
    # 反向
    # res = models.Publish.objects.filter(book__pk=1).values('name', 'book__title')
    # print(res)

    # 反向
    # 查询书籍主键为1的作者姓名
    # res = models.Book.objects.filter(pk=1).values('title', 'authors__name')
    # print(res)

    # 反向
    # 获取作者名为jason的作者详情
    # res = models.AuthorDetail.objects.filter(author__name='jason').values('phone', 'author__name')
    # print(res)

    # 查询书籍主键为1的作者手机号，涉及到三张表
    # book, author, author_detail
    # 先跨到author表，再从author表跨到author_detail
    # res = models.Book.objects.filter(pk=1).values('authors__author_detail__phone')
    # print(res)

    # 聚合查询, 五个聚合查询的使用, aggregate
    # 聚合查询都是配合分组一起使用的
    from django.db.models import Max, Min, Sum, Count, Avg

    # 统计书的平均价格
    # res = models.Book.objects.aggregate(Avg('price'))
    # print(res)

    # 一次性使用上述方法
    # res = models.Book.objects.aggregate(Avg('price'), Min('price'), Sum('price'), Count('price'))
    # print(res)

    # 统计每一本书的作者个数, 分组关键字annotate
    # res = models.Book.objects.annotate(author_num=Count('authors')).values('title', 'author_num')  # models后面是什么就按照什么分组， author_num未别名
    # author_num是自定义的变量，用来存储作者个数
    # print(res)

    # 统计每个出版社最便宜的书的价格
    # res = models.Publish.objects.annotate(min_price=Min('book__price')).values('name', 'min_price')
    # print(res.query)

    # 统计不止一个作者的图书
    # 1.先按照图书分组,求出每一本书对应的作者的个数
    # 然后过滤出不止一个作者的图书
    # res = models.Book.objects.annotate(author_num=Count('authors')).filter(author_num__gt=1).values('title', 'author_num')
    # print(res)
    '''
    只要orm结果是QuerySet类型，都可以继续.values或者.filter
    '''

    # 4.查询每个作者出的书的总价格
    # res = models.Author.objects.annotate(sum_price=Sum('book__price')).values('name', 'sum_price')
    # print(res)

    # 按照指定的字段分组
    # models.Book.objects.values('price').annotate()

    # F与Q查询
    # 查询卖出数大于库存数的书籍
    # 当要比较的数不是固定的，而是表中的某一个字段，就要使用F与Q查询
    # F的功能能帮你直接获取到表中某个字段的数据，可以用作比较条件
    from django.db.models import F
    # res = models.Book.objects.filter(sold__gt=F('inventory'))
    # print(res)

    # 将所有数据的价格提升50
    # models.Book.objects.update(price=F('price') + 50)

    # 将所有数的名字后面加上爆款两个字
    # 在操作字符串类型的数据的时候，F不能够直接做到字符串的拼接
    # 需要使用Concat
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # models.Book.objects.update(title=Concat(F('title'), Value('爆款')))

    # Q查询
    # 1.查询卖出数大于100或者价格小于600的书籍
    # res = models.Book.objects.filter(sold__gt=100, price__lt=600).values('price', 'sold')
    # filter内多个参数是and连接
    # 想要使用OR，需要用到Q查询
    from django.db.models import Q
    # res = models.Book.objects.filter(Q(sold__gt=100), Q(price__lt=600)) # Q包裹逗号分开，还是and关系
    # res = models.Book.objects.filter(Q(sold__gt=100)|Q(price__lt=600)) # |表示OR关系
    # res = models.Book.objects.filter(~Q(sold__gt=100)|Q(price__lt=600))  # ~表示非(NOT) 关系
    # print(res)

    # Q的高阶用法,如用户输入搜索条件
    # 生成对象
    # q = Q()
    # q.connector = 'or', # 修改连接条件为or
    # 构造查询条件如 sold > 100
    # q.children.append(('sold__gt', 100))
    # q.children.append(('price__lt', 600))
    # res = models.Book.objects.filter(q) # filter括号内支持直接放Q对象，默认还是and关系
    # print(res)


    # 事务
    # from django.db import transaction
    # 开启事务
    # try:
    #     with transaction.atomic():
    #         # with代码块内所有的代码都属于一个事务
    #         pass
    # except Exception as e:
    #     print(e)
    #
    # print('执行其他操作')


    # 实现获取到的是一个数据对象，通过点就能够拿到书名，价格
    # res = models.Book.objects.only('title')
    # res_1 = models.Book.objects.all()
    # print(res)
    # for i in res:
    #     print(i.price)

    # res = models.Book.objects.defer('title')
    # print(res)
    # for i in res:
    #     print(i.price)

    """
    defer 与 only刚好相反
    defer括号内存放的字段不在查询出的对象里面，查询该字段需要重新走数据
    而如果查询的是非括号内的字段，则不需要走数据库了
    """

    # select_related 与prefetch_related  跨表操作有关
    res = models.Book.objects.all()
    for i in res:
        print(i.publish.name)  # 每循环一次都要走一次数据库查询

    res_1 = models.Book.objects.select_related('publish')
    print(res_1)
    for i in res_1:
        print(i.publish.addr)
    """
    select_related内部直接先将book与publish连起来，然后一次性
    将大表里面所有的数据封装给查询出来的对象
    注意：select_related括号内只能存放外键字段，一对多，一对一，多对多不可以
    """
    res_2 = models.Book.objects.prefetch_related('publish')
    for i in res_2:
        print(i.publish.name)




























