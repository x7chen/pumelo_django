from django.shortcuts import render
from django.http import HttpResponse
from models import Goods
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse(u'''{
"employees": [
{ "firstName":"Bill" , "lastName":"Gates" },
{ "firstName":"George" , "lastName":"Bush" },
{ "firstName":"Thomas" , "lastName":"Carter" }
]
}''', content_type='application/json')


def db_add(request):
    goods = Goods(name="pumeloes")
    goods.price = '12.3'
    goods.barcode = '123456789'
    goods.package = 'box'
    goods.level = 'one'
    goods.origin = 'china'
    goods.unit = '500g'
    goods.save()
    return HttpResponse("success")


def db_read(request):
    # goods = Goods.objects.get(id=3)
    goods_id = int(request.POST("goods_id").encode("ascii"))
    # goods = get_object_or_404(Goods, pk=goods_id)
    goods = Goods.objects.get(id=goods_id)
    return HttpResponse(goods.toJSON())
