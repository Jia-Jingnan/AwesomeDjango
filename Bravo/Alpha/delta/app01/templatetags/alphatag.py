from django import template


register = template.Library()


# 自定义过滤器，最多只能有两个参数
@register.filter(name='alpha')
def my_sum(a, b):
    return a + b


# 自定义标签,可以有多个参数
@register.simple_tag(name='bravo')
def index(a,b,c,d):
    return '%s-%s-%s-%s'%(a,b,c,d)



@register.inclusion_tag('left_menu.html')
def left(n):
    data = ['第{}项'.format(i) for i in range(n)]
    return locals() # 将data传递给left_menu.html