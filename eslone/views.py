from django.shortcuts import render
from django.http import HttpResponse
from models import Goods


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
    goods.save()
    return HttpResponse("success")


def db_read(request):
    goods = Goods.objects.get(id=1)
    return HttpResponse(goods.toJSON())
