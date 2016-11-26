from django.test import TestCase
from django.http import HttpResponse
from models import Goods


# Create your tests here.
def db_add(request):
    goods = Goods
    goods.name = "柚子"
    goods.save()
    return HttpResponse("添加成功")


def db_read(reqest):
    goods = Goods.objects.get(0)
    return HttpResponse(goods.name)
