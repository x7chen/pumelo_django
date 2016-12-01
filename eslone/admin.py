from django.contrib import admin
from models import *


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_filter = ['barcode']
    search_fields = ['barcode']
    fields = ['name', 'price', 'package', 'origin', 'barcode']
    list_display = ('name', 'price', 'package', 'origin', 'barcode')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodLogs)
