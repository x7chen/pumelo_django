from django.contrib import admin
from models import *


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    # 可编辑的表单
    fields = ['name', 'price', 'package', 'origin', 'barcode']
    # 显示的字段
    list_display = ('name', 'price', 'package', 'origin', 'barcode')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodLogs)
