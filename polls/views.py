from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q, Sum, Count

from polls.models import Product


def index(request):
    # # 数据插入的两种方式
    # Product.objects.create(name='oyty', weight='111g', size='120*75*77', type_id=1)
    #
    # p = Product(name='oyty', weight='111g', size='120*75*77', type_id=1)
    # p.save()
    #
    # # 数据更新
    # p = Product.objects.get(id=9)
    # p.name = 'haha'
    # p.save()
    #
    # # 更新单条数据
    # Product.objects.get(id=9).update(name='haha')
    # # 更新多条数据
    # Product.objects.filter(name='oyty').update(name='haha')
    # # 无过滤条件，全表更新
    # Product.objects.update(name='haha')
    #
    # # 删除数据
    # # 删除全部
    # Product.objects.all().delete()
    # Product.objects.get(id=9).delete()
    # # 删除多条
    # Product.objects.first(name='oyty').delete()
    #
    # # 查询数据
    # # 查询全部, 返回数组
    # p = Product.objects.all()
    # 'select * from product'
    #
    # # 查询前5条
    # p = Product.objects.all()[:5]
    # 'select * from product limit 5'
    #
    # # 查询某个字段
    # p = Product.objects.values('name')
    # 'select name from product'
    #
    # # values_list 方法，以列表表示返回数据，列表元素以元组格式表示
    # p = Product.objects.values_list('name')[:3]
    #
    # # get方法查询数据
    # p = Product.objects.get(id=2)
    # 'select * from product where id=2'
    #
    # # filter方法查询数据, 返回数组
    # p = Product.objects.filter(id=2)
    #
    # # 多条件查询
    # p = Product.objects.filter(name='oyty', id=9)
    #
    # # or查询，需要引入Q，格式为：Q(field=value) | Q(field=value)
    # p = Product.objects.filter(Q(name='oyty') | Q(id=9))
    # 'select * from product where name="oyty" or id=9'
    #
    # # count方法统计查询数据的数据量
    # p = Product.objects.filter(name='oyty').count()
    # p = 2
    #
    # # 去重查询，distinct
    # p = Product.objects.values('name').filter(name='oyty').distinct()
    # 'select DISTINCT name from product where name="oyty"'
    #
    # # 根据id降序排列, 降序只要在order_by里面的字段前面加上"-"即可
    # p = Product.objects.order_by('-id')
    #
    # # 聚合查询, 实现对数据值求和，求平均值等，Django提供annotate和aggregate方法实现
    # p = Product.objects.values('name').annotate(Sum('id'))
    # 'select name, sum(id) as "id_sum" from product group by name order by null'
    #
    # # aggregate将某个字段的值进行计算并返回计算结果
    # p = Product.objects.aggregate(id_count=Count('id'))
    # {'id_count': 11}
    # 'select COUNT(id) as "id_count" from product'

    return HttpResponse("Hello, world, You're at the polls index.")
