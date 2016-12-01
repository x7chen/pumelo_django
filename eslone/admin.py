from django.contrib import admin
from models import *


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'package', 'origin', 'barcode']


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodLogs)
