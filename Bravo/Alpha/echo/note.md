### 今日内容详细  
#### 单表操作
```python
# django自带的sqlite3数据库对日期格式不敏感，处理的时候容易出错
```
#### 测试脚本
```python
# 当只是想测试django模型，可以通过test单元测试实现
# 测试环境的准备
```

#### 查看内部SQL语句的方式
```python
# <QuerySet [('God of Thunder', 1300), ('God of mischeif', 1290)]>
res = models.User.objects.values_list('name', 'age')
# 查看内部的sql语句,这种查看SQL语句的方式只能用于queryset
print(res.query)
# 方式二：去配置文件中配置显示SQL语句
```

#### 神奇的双下划綫查询



#### 一对多外键增删改查


#### 多对多外键增删改查